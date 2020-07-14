import {request} from './request_singleBook'

export function getSingleBookmultdata () {
	return request({
		url: '/api/bookdetail/'
	})

}

export function getCollectionmultdata () {
	return request({
		url: '/api/collection/'
	})

}