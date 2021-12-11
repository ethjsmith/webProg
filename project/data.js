var sqlite3 = require('sqlite3').verbose();
var db = new sqlite3.Database('comments.db');

db.serialize(function() {
//  db.run("DROP TABLE comments");
  db.run("CREATE TABLE comments (id INTEGER PRIMARY KEY AUTOINCREMENT, dt TEXT)");

  var stmt = db.prepare("INSERT INTO comments(dt) VALUES (?)");
  var n = "great site! "
  stmt.run(n);
  stmt.finalize();

  db.all("SELECT id, dt FROM comments", function(err, row) {
      console.log(row);
  });
});

db.close();
