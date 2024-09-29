const router = require("express").Router();
let User = require("../schemas/user");

router.route("/").get(async function (req, res) {
 
  User.find({})
    .then((users) => res.json(users))
});

router.route("/test").get(async function (req, res) {
  res.json({"msg":"hello"})
});

router.route("/add").post(async function (req, res) {
  // Check if the user already exists based on the email
  const exists = await User.findOne({ email: req.body.email });
  if (exists) {
      res.json("User already exists");
      return;
  }
  
  const newUser= new User({
      fullName: req.body.fullName, 
      email: req.body.email,
      password: req.body.password
  });

  newUser
      .save()
      .then(() => res.json("User added!"))
      .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/:username").get((req, res) => {
  User.find({ username: req.params.username })
    .then((users) => res.json(users))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/:username").delete((req, res) => {
  User.findOneAndDelete({ username: req.params.username })
    .then(() => res.json("User deleted."))
    .catch((err) => res.status(400).json("Error: " + err));
});

router.route("/update/:username").post(async (req, res) => {
  if ((await auth(req, ["admin"])) !== 1) {
    res.status(403).json("Auth Error");
    return;
  }
  const exists = await User.findOne({ username: req.body.username });
  if (exists && req.body.username != req.params.username) {
    res.status(400).json("User already exists");
    return;
  }
  User.findOne({ username: req.params.username })
    .then(async (user) => {
      const hashedPassword = undefined;
      const salt = await bcrypt.genSalt(10);
      if (req.body.password) {
        hashedPassword = await bcrypt.hash(req.body.password, salt);
      }
      User.replaceOne(
        { username: req.params.username },
        {
          username: req.body.username || user.username,
          password: hashedPassword || user.password,
          firstName: req.body.firstName || user.firstName,
          lastName: req.body.lastName || user.lastName,
          email: req.body.email || user.email,
          phone: req.body.phone || user.phone,
          permission: req.body.permission || user.permission,
          created: user.created,
          updated: Date.now,
        }
      )
        .then(() => res.json("User updated!"))
        .catch((err) => res.status(400).json("Error: " + err));
    })
    .catch((err) => res.status(400).json(err));
});


router.route("/login").post(async function (req, res) {
  const user = await User.findOne({ username: req.body.username });
  if (!user) {
    res.status(400).json("incorrect credentials");
    return;
  }
  if (!req.body.password) {
    res.status(400).json("incorrect credentials");
    return;
  }
  const hashedPassword = user.password;
  const match = await bcrypt.compare(req.body.password, hashedPassword);
  if (!match) {
    res.status(400).json("incorrect credentials");
  } else {
    const userDB = await User.findOne({ username: req.body.username });
    res.status(200).json({
      message: "login success",
      token: createToken(req.body.username, userDB.permission),
      user: req.body.username,
      id: userDB._id,
      perm: userDB.permission,
    });
  }
});
module.exports = router;
