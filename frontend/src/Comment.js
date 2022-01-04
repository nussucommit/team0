import { useState } from "react";
import { useHistory } from "react-router-dom";
import CommentDetails from "./CommentDetails";

const Comment = () => {

    // const author = how to set author to be the logged in user;
    const [CommentBody, setCommentBody] = useState('');
    const [isPending, setIsPending] = useState(false);
    const history = useHistory();

    const handleSubmit = (e) => {
        e.preventDefault();
        const comment = { CommentBody };
        // only display comments for each post based on the id

        setIsPending(true);
        
        fetch('http://localhost:8000/comments', {
            method: 'POST',
            headers: { "Content-Type": "application/json"},
            body: JSON.stringify(comment) /* add new blog to the json server */
        }).then(() => {
            setIsPending(false);
            // history.go(-1);
            // history.push('/blogs/:id');
        })

    }
    return ( 
        <div className="comment">
            <h4>Comments</h4>
            <form onSubmit={handleSubmit}>
                <textarea 
                    required
                    value={CommentBody}
                    onChange={(e) => setCommentBody(e.target.value)}
                    placeholder="Write your comment..."
                ></textarea>
                { !isPending && <button>Post</button> }
                { isPending && <button disabled>Posting...</button> }
             </form>
            <div className="comment-details">
                <CommentDetails />
            </div>
        </div>
     );
}
 
export default Comment ;