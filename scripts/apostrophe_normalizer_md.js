const fs = require("node:fs");

const replaceChars = (str) =>
  str
    .replaceAll(/(([oOgG])')/gm, "$2ʻ")
    .replaceAll(/(([aAbBdDeEfFhHiIjJlLmMnNqQrRsStTuUyYzZ])')/gm, "$2ʼ");

for (const filepath of fs.globSync("**/*.md")) {
  const content = fs.readFileSync(filepath).toString();
  const newContent = replaceChars(content);
  fs.writeFileSync(filepath, newContent);
}
