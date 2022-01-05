import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import api from "./api";
import { useHistory } from "react-router-dom";

const Login = ({ login }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [re_password, setre_Password] = useState("");
  const history = useHistory();

  return (
    <>
      <div className="home"></div>
      <div className="Login">
        <h1>Sign Up</h1>
        <div>
          <input
            type="text"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <input
            type="password"
            value={re_password}
            onChange={(e) => setre_Password(e.target.value)}
          />
          <button
            onClick={() => {
              api
                .post("auth/users/", {
                  username: username,
                  password: password,
                  re_password: re_password,
                })
                .then((res) => {
                  history.push("/login");
                })
                .catch((err) => {
                  alert(err);
                });
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
