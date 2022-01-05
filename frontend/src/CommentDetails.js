import { useHistory, useParams } from "react-router-dom";
import useFetch from "./useFetch";

const CommentDetails = () => {

    const { blogTitle } = useParams();
    const { data: comment, error, isPending } = useFetch('http://localhost:8000/comments/' + blogTitle);
    const history = useHistory();

    const handleClick = () => {
        fetch('http://localhost:8000/comments/' + comment.blogTitle, {
            method: 'DELETE'
        }).then( () => {
            history.push('/')
        })
    }

    return ( 
        <div className="comment-details">
        { isPending && <div> Loading...</div> }
        {error && <div>{ error }</div> }
        { comment && (
            <article>
                <h2>{ comment.cbody }</h2>
                <p>Written by { comment.cauthor }</p>
                <div>{ comment.cbody }</div>
            </article>
        )}
        </div>
     );
}
 
export default CommentDetails ;