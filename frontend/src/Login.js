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
      <div className="home"></div>
      <div className="Login">
        <h1>Login</h1>
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
            Login
          </button>
        </div>
      </div>
    </>
  );
};

export default Login;
