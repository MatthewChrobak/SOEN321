const fs = require('fs');
const _ = require('lodash');
const knex = require('knex');

// 1. Builds the database connection with the knexjs library
function getConnection(filename) {
    return knex({
        client: 'sqlite3',
        connection: {
            filename: filename
        }
    });
}

// 2. Get all database connections
const comparing = 'Chun_Home.sqlite';
const subjects = [
    'Burger_King.sqlite',
    'Concordia.sqlite',
    'Mail_Champlain.sqlite',
    'Parc_de_la_Cite.sqlite',
    'Tim_Hortons.sqlite'
];
const connections = [
    comparing,
    ...subjects
].map((filename) => getConnection(filename));

// 3. Select all data from moz_cookies and resolve data
const data = Promise.all(connections.map((connection) => {
    return connection
        .select().from('moz_cookies');
})).then((data) => {
    connections.forEach((connection) => connection.destroy());

    return data;
});

// 4. Prepare data by removing some unnecessary attributes
const transformed = data.then((tables) => {
    return tables.map((table) => {
        let current = {};

        table.forEach((row) => {
            current[row.name] = {
                baseDomain: row.baseDomain,
                originAttributes: row.originAttributes,
                value: row.value,
                host: row.host,
                path: row.path,
                isSecure: row.isSecure,
                isHttpOnly: row.isHttpOnly,
                isBrowserElement: row.isBrowserElement,
                sameSite: row.sameSite
            }
        });

        return current;
    });
});

// 4. Generate report.
transformed.then(tables => {
    let compare = tables.shift(); // Get the first table that we are going to compare with.
    let names = Object.keys(compare); // Get the array of all all cookie names

    let report = {};

    tables.forEach((table) => {
        let cookies = {
            removed: {},
            new: {}
        };

        names.forEach((name) => {
            if (table[name] === undefined) {
                cookies.removed[name] = compare[name];
            }
        });

        _.difference(Object.keys(table), names)
            .forEach((name) => {
                cookies.new[name] = table[name];
            });

        report[subjects.shift()] = cookies;
    });

    fs.writeFileSync('report.json', JSON.stringify(report, null, '\t'));
});