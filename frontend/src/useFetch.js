import{ useState, useEffect } from 'react';

const useFetch = (url) => {
    const [data, setData] = useState(null);
    const[isPending, setIspending] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const abortCont = new AbortController();

        fetch(url, { signal: abortCont.signal })
            .then(res => {
                if (!res.ok){
                    throw Error('could not fetch the data for that resource');
                }
                return res.json()
             })
            .then((data) => { /* 'data' here is a local variable */
                setData(data);
                setIspending(false);
                setError(null);
        })
        .catch(err => {
            if(err.name === 'AbortError') {
                console.log('fetch aborted')
            }else {
                setIspending(false);
                setError(err.message); /*connection error*/
            }
         });

         return () => abortCont.abort();
    
    }, [url]); // fires on every render, but may end up in infinitely loop when there is a change in the State

    return{ data, isPending, error };
}

export default useFetch;