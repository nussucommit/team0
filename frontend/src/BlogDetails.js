import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";

const BlogDetails = () => {
  const { id } = useParams();
  const {
    data: blog,
    error,
    isPending,
  } = useFetch("http://localhost:8000/post/" + id);
  const history = useHistory();

  const handleClick = () => {
    fetch("http://localhost:8000/post/" + blog.id, {
      method: "DELETE",
      headers: {
        Authorization: `Basic ${localStorage.getItem("token")}`,
      },
    }).then(() => {
      history.push("/");
    });
  };

  return (
    <div className="blog-details">
      {isPending && <div> Loading...</div>}
      {error && <div>{error}</div>}
      {blog && (
        <article>
          <h2>{blog.title}</h2>
          <p>Written by {blog.user}</p>
          <div>{blog.content}</div>
          <button onClick={handleClick}>delete</button>
        </article>
      )}
    </div>
  );
};

export default BlogDetails;
