import {request} from './request_singleBook'

export function getSingleBookmultdata () {
	return request({
		url: '/api/bookdetail/',
		params:{
			book_id:"carqdIdfVlYC"
		}
	})

}

export function getCollectionmultdata () {
	return request({
		url: '/api/collection/'
	})

}

export function getSearchResult (query) {
	return request({
		url: '/api/searchbook/',
		method:'post',
		params:query
	})

}