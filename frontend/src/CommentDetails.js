import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";
import BlogDetails from "./BlogDetails";
import { useEffect, useState } from "react";
import api from "./api";

const CommentDetails = () => {
  const { id } = useParams();
  const { blogTitle } = useParams();
  const {
    data: comment,
    error,
    isPending,
  } = useFetch("http://localhost:8000/post/comments/" + id);
  const history = useHistory();

  const handleClick = () => {
    fetch("http://localhost:8000/post/comments/" + id, {
      method: "DELETE",
    }).then(() => {
      history.push("/");
    });
  };

  return (
    <div className="comment-details">
      {isPending && <div> Loading...</div>}
      {error && <div>{error}</div>}
      {comment &&
        comment.map((e) => {
          return (
            <article>
              <h2>{e.user}</h2>
              <p>{e.content}</p>
              <div></div>
            </article>
          );
        })}
    </div>
  );
};

export default CommentDetails;
