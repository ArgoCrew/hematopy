import Api from '@/services/Api'

export default {

  createBanner (params) {
    const url = 'recipient'
    const headers = { 'Content-Type': 'multipart/form-data' }
    return Api(url, 'post', headers, params)
  }
}
