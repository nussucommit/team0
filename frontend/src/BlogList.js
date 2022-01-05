import { Link } from "react-router-dom";
import { useState, useEffect } from "react";
import api from "./api";

const BlogList = ({ title }) => {
  const [blogs, setBlogs] = useState("");

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
          setBlogs(res.data);
        } else {
          console.log("error");
        }
      });
  };

  useEffect(() => {
    getResults();
  }, []);

  return (
    <div className="blog-list">
      <h2>{title}</h2>
      {blogs
        ? blogs.map((blog) => (
            <div className="blog-preview" key={blog.id}>
              <Link to={`/blogs/${blog.id}`}>
                {" "}
                {/* template string can output the variable inside it */}
                <h2>{blog.title}</h2>
                <p>Written by {blog.user}</p>
              </Link>
            </div>
          ))
        : false}
    </div>
  );
};

export default BlogList;
