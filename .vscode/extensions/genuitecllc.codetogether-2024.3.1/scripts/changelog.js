'use strict';

const fs = require('fs');
let rawdata = fs.readFileSync('../../../RELEASES_CODETOGETHER.json');
let json = JSON.parse(rawdata);
console.log(json);
var changelog = '# Change Log\nCodeTogether is available for VS Code, Eclipse, and IntelliJ providing pair programming services right from a browser.\n';

let versions = json["log"];
for (var i = 0; i < versions.length; i++) {
    let ver = versions[i];
    changelog += '\n## [';
    changelog += ver["version"];
    changelog += '] - ';
    changelog += ver["date"];
    changelog += '\n';//### Improvements\n';
    let changes = ver["notes"];
    for (var j = 0; j < changes.length; j++) {
        let change = changes[j];
        changelog += '- **';
        changelog += change["title"];
        changelog += '**  \n  ';
        changelog += change["description"];
        changelog += '\n';
    }
}


fs.writeFileSync('CHANGELOG.md', changelog);
