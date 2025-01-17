const mongoose = require("mongoose");
const Schema = mongoose.Schema;

const userSchema = new Schema({
  id: { type: Number, unique: true },  // Optional, assuming you'll manage IDs manually
  fullName: { type: String, required: true }, // Required
  gender: { type: String }, // Optional
  age: { type: Number }, // Optional
  phoneNumber: { type: String }, // Optional
  homeTown: { type: String }, // Optional
  state: { type: String }, // Optional
  department: { type: String }, // Optional
  roomTemp: { type: Number }, // Optional
  selfCleanliness: { type: String }, // Optional
  selfGuests: { type: String }, // Optional
  selfLoudness: { type: String }, // Optional
  roommateInteraction: { type: String }, // Optional
  selfSleepTime: { type: String }, // Optional
  selfMajor: { type: String }, // Optional
  pictureName: { type: String }, // Optional
  roommateMajor: { type: String }, // Optional
  roommateGuests: { type: String }, // Optional
  roommateLoudness: { type: String }, // Optional
  bio: { type: String }, // Optional
  email: { type: String, required: true, unique: true }, // Required
  password: { type: String, required: true } // Required
});

// Create the User model
const User = mongoose.model("Users", userSchema);

// Export the User model
module.exports = User;
