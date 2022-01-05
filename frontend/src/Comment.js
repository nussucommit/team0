import { useState } from "react";
import { useHistory, useParams } from "react-router-dom";
import CommentDetails from "./CommentDetails";
import BlogDetails from "./BlogDetails";
import api from "./api";

const Comment = () => {
  const { id } = useParams();
  // const author = how to set author to be the logged in user;
  const username64 = localStorage.getItem("token");
  const username = atob(username64).split(":").at(0);
  const [CommentBody, setCommentBody] = useState("");
  const [isPending, setIsPending] = useState(false);
  const history = useHistory();

  const [dataId, setDataId] = useState(0);

  return (
    <div className="comment">
      <h4>Comments</h4>
      <form>
        <textarea
          required
          value={CommentBody}
          onChange={(e) => setCommentBody(e.target.value)}
          placeholder="Write your comment..."
        ></textarea>
        {
          <button
            onClick={(e) => {
              e.preventDefault();
              api
                .post(
                  "/comment/create",
                  {
                    user: username,
                    post: id,
                    content: CommentBody,
                  },
                  {
                    headers: {
                      Authorization: `Basic ${localStorage.getItem("token")}`,
                    },
                  }
                )
                .then(() => {
                  setDataId((i) => i + 1);
                });
            }}
          >
            Post
          </button>
        }
        {isPending && <button disabled>Posting...</button>}
      </form>
      <div className="comment-details">
        <CommentDetails key={dataId} />
      </div>
    </div>
  );
};

export default Comment;
