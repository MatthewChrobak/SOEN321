const report = require('./report.json');
const locations = Object.keys(report);

locations.forEach((location) => {
   const removed = Object.keys(report[location].removed).length;
   const added = Object.keys(report[location].added).length;

   console.log(location);
   console.log(`- removed \t ${removed}`);
   console.log(`+ added \t ${added}\n`);
});
