const express = require("express");
const router = express.Router();
const User = require("../models/customerSchema");
var moment = require("moment");
const userController = require("../controllers/userController");


// GET Requst

router.get("/", userController.user_login_get);
router.get("/index", userController.user_index_get);

router.get("/edit/:id", userController.user_edit_get);

router.get("/view/:id", userController.user_view_get);

router.get("/signup", userController.user_signup_get);

// POST Requst
router.post("/search", userController.user_search_post);
router.post("/signup", userController.user_signup_post);
router.post("/login", userController.user_login_post);

// DELETE Request
router.delete("/edit/:id", userController.user_delete);

// PUT Requst
router.put("/edit/:id", userController.user_put);

module.exports = router;
