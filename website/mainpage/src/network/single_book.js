import {request} from './request_singleBook'

export function getSingleBook_multdata () {
	return request({
		url: '/api/single_book'
	})

}