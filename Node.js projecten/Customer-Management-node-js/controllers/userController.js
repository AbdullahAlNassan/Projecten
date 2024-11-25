const { User, login } = require("../models/customerSchema");
var moment = require("moment");
const bcrypt = require("bcrypt");

const user_index_get = (req, res) => {
  // result ==> array of objects
  console.log("--------------------------------------------");
  User.find()
    .then((result) => {
      res.render("index", { arr: result, moment: moment });
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_login_get = (req, res) => {
  res.render("user/login");
};

const user_signup_get = (req, res) => {
  res.render("user/signup");
};

const user_edit_get = (req, res) => {
  User.findById(req.params.id)
    .then((result) => {
      res.render("user/edit", { obj: result, moment: moment });
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_view_get = (req, res) => {
  // result ==> object
  User.findById(req.params.id)
    .then((result) => {
      res.render("user/view", { obj: result, moment: moment });
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_search_post = (req, res) => {
  console.log("*******************************");

  const searchText = req.body.searchText.trim();

  User.find({ $or: [{ fireName: searchText }, { lastName: searchText }] })
    .then((result) => {
      console.log(result);
      res.render("user/search", { arr: result, moment: moment });
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_delete = (req, res) => {
  User.deleteOne({ _id: req.params.id })
    .then((result) => {
      res.redirect("/index");
      console.log(result);
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_put = (req, res) => {
  User.updateOne({ _id: req.params.id }, req.body)
    .then((result) => {
      res.redirect("/index");
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_add_get = (req, res) => {
  res.render("user/add");
};

const user_post = (req, res) => {
  User.create(req.body)
    .then(() => {
      res.redirect("/index");
    })
    .catch((err) => {
      console.log(err);
    });
};

const user_signup_post = (req, res) => {
  const { username, password } = req.body;

  login
    .findOne({ name: username })
    .then((existingUser) => {
      if (existingUser) {
        return res
          .status(400)
          .send("User already exists. Please choose a different username.");
      }

      return bcrypt.hash(password, 10).then((hashedPassword) => {
        const newUser = new login({ name: username, password: hashedPassword });
        return newUser.save();
      });
    })
    .then(() => res.redirect("/"))
    .catch((err) => {
      console.log(err);
    });
};

const user_login_post = async (req, res) => {
  try {
    // Controleer of de gebruiker bestaat
    const check = await login.findOne({ name: req.body.username });
    if (!check) {
      // Algemene foutmelding om beveiliging te verbeteren
      return res.status(400).send("Incorrect username or password.");
    }

    // Vergelijk het ingevoerde wachtwoord met het gehashte wachtwoord
    const isPasswordMatch = await bcrypt.compare(
      req.body.password,
      check.password
    );
    if (isPasswordMatch) {
      // Redirect naar index (of gebruik sessies/jwt voor authenticatie)
      res.redirect("index");
    } else {
      // Fout bij wachtwoord
      res.status(400).send("Incorrect username or password.");
    }
  } catch (error) {
    console.error(error);
    // Algemene foutmelding
    res.status(500).send("An error occurred while processing your request.");
  }
};

module.exports = {
  user_index_get,
  user_edit_get,
  user_view_get,
  user_search_post,
  user_delete,
  user_put,
  user_add_get,
  user_post,
  user_login_get,
  user_signup_get,
  user_signup_post,
  user_login_post,
};
