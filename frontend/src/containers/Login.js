import React, { useState } from "react";
import "./Login.css";

export default function Login() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const validatediv = () => {
    return email.length > 0 && password.length > 0;
  }


  const submit = () => {
    console.log(email, password);
    axios.post('/user', {
      firstName: 'Fred',
      lastName: 'Flintstone'
    })
    .then(function (response) {
      console.log(response);
    })
    .catch(function (error) {
      console.log(error);
    });
  
  }

  return (
    <div className="Login">
      <div>
        <div size="lg" controlId="email">
          <label>Email</label>
          <input
            autoFocus
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div size="lg" controlId="password">
          <label>Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>
        <button block size="lg" type="submit" disabled={!validatediv()} onClick={() => submit()}>
          Login
        </button>
      </div>
    </div>
  );
}