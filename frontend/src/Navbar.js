import { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Navbar = ({ isLoggedIn, logout }) => {
  return (
    <nav className="navbar">
        <h1>Team 0</h1>
      <div className="links">
        {/* <a href="/">Home</a> */}
        {isLoggedIn ? (
          <>
            <Link to="/">Home</Link>
            <Link
              to="/create"
              style={{
                color: "white",
                backgroundColor: "#f1356d",
                borderRadius: "8px",
              }}
            >
              New Blog
            </Link>{" "}
            {/** first curly brace means dynamic value, inner one for js obeject */}
            <Link
              to="/login"
              onClick={() => {
                localStorage.removeItem("token");
                logout();
              }}
            >
              Log out
            </Link>
          </>
        ) : (
          <div className="links">
            <Link to="/login">Log in</Link>
          </div>
        )}
      </div>
    </nav>
  );
};

export default Navbar;
