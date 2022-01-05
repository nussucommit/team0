import { useState } from "react";
import { useHistory } from "react-router-dom";
import api from "./api";
import { Link } from "react-router-dom";

const Create = () => {
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [isPending, setIsPending] = useState(false);

  const history = useHistory();
  const username64 = localStorage.getItem("token");
  const username = atob(username64).split(":").at(0);

  return (
    <div className="create">
      <h2>Add a New Blog</h2>
      <form>
        <label>Blog title:</label>
        <input
          type="text"
          required
          value={title}
          onChange={(e) =>
            setTitle(e.target.value)
          } /* change the value of title every time smth is typed */
        />
        <label>Blog body:</label>
        <textarea
          required
          value={body}
          onChange={(e) => setBody(e.target.value)}
        ></textarea>
        {!isPending && (
          <button
            onClick={(e) => {
              e.preventDefault();
              // id, user, title, content
              api.post(
                `/post/create`,
                {
                  user: username,
                  title: title,
                  content: body,
                },
                {
                  headers: {
                    Authorization: `Basic ${localStorage.getItem("token")}`,
                  },
                }
              );
              history.push("/");
            }}
          >
            Add Blog
          </button>
        )}
        {isPending && <button disabled>Adding blog...</button>}
      </form>
    </div>
  );
};

export default Create;
