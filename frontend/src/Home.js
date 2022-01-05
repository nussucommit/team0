import BlogList from "./BlogList";
import useFetch from "./useFetch";
import UserList from "./UserList";
import { useState, useEffect } from "react";
import api from "./api";

const Home = () => {
  const {
    data: blogs,
    isPending,
    error,
  } = useFetch("http://localhost:8000/blogs");

  return (
    <div className="home">
      <BlogList title="All Blogs!" />
    </div>
  );
};

export default Home;
