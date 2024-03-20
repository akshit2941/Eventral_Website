import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";

const firebaseConfig = {
  apiKey: "Your API Here",
  authDomain: "Your API Here",
  projectId: "Your API Here",
  storageBucket: "Your API Here",
  messagingSenderId: "Your API Here",
  appId: "Your API Here",
  measurementId: "Your API Here"
};

const app = initializeApp(firebaseConfig);
const auth = getAuth(app)



export { app, auth };
