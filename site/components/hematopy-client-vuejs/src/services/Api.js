import axios from 'axios'

const instance = axios.create({
  // baseURL: `https://hematopy-dev-gustavorps.herokuapp.com/api/v1/`
  baseURL: `http://localhost:3003/`
})

export default(url, method, headers, params) => {
  return instance({
    method,
    headers,
    url,
    ...method === 'post' || method === 'put' ? { data: params } : { params }
  })
}
