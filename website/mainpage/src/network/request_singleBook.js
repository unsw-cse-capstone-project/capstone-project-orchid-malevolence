import axios from 'axios'

export function request (config) {
	//create instance of axios
	const instance=axios.create({
		baseURL:'http://127.0.0.1:8000',
		timeout:4000

	})
	//axios  interceptor request
	instance.interceptors.request.use(config=>{
		return config
	},error => {

		})
	//axios  interceptor response
	instance.interceptors.response.use(res=>{
		return res.data
	},error => {

	})
	// real request
	return instance(config)

}