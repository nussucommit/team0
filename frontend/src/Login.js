import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import api from "./api";
import { useHistory } from "react-router-dom";

const Login = ({ login }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const history = useHistory();

  return (
    <>
      <div className="login">
        <h1>Log In</h1>
        <div>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Username"
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Password"
          />
          <button
            onClick={() => {
              api
                .post("/auth/token/login", {
                  username: username,
                  password: password,
                })
                .then((res) => {
                  console.log(res.data);
                  console.log(res.status);
                  if (res.status == 200) {
                    const basicString = `${username}:${password}`;
                    const basicBase64 = btoa(basicString);
                    localStorage.setItem("token", basicBase64);

                    login();
                    history.push("/");
                  }
                })
                .catch((err) => {
                  alert("Wrong Username or Password");
                });
            }}
          >
            Log In
          </button>
        </div>
        <hr />
        <div>
          <button
            onClick={() => {
              history.push("/SignUp");
            }}
          >
            Sign Up
          </button>
        </div>
      </div>
    </>
  );
};

export default Login;
