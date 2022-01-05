import { useState, useEffect } from "react";

import { Link } from "react-router-dom";
import api from "./api";

const UserList = ({ blogs, title }) => {
  const [users, setUsers] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const getResults = () => {
    api
      .get("/results", {
        headers: {
          Authorization: `Basic ${localStorage.getItem("token")}`,
        },
      })
      .then((res) => {
        if (res.status == 200) {
          console.log(res.data);
          setUsers(res.data);
        } else {
          console.log("error");
        }
      });
  };

  useEffect(() => {
    getResults();
  }, []);

  return (
    <div className="user-list">
      <h1>USERS API</h1>
      {users
        ? users.map((user) => (
            <>
              <h3>{user.email}</h3>
              <p>{`${user.first_name} and ${user.last_name}`}</p>
            </>
          ))
        : false}

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
            const basicString = `${username}:${password}`;
            const basicBase64 = btoa(basicString);
            localStorage.setItem("token", basicBase64);
            getResults();
          }}
        >
          Login
        </button>
      </div>
    </div>
  );
};

export default UserList;
