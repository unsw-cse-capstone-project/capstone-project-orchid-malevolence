import {request} from './request_singleBook'

export function getSingleBookmultdata (query) {
	return request({
		url: '/api/bookdetail/',
		params:query
	})

}

export function getCollectionmultdata () {
	return request({
		url: '/api/collection/'
	})

}

export function getperinfodata () {
	return request({
		url: '/api/account/'
	})

}

export function getSearchResult (query) {
	return request({
		url: '/api/searchbook/',
		method:'post',
		data:query
	})

}

export function postperinfo (data) {
	return request({
		url: '/api/account/',
		method:'post',
		data:data
	})

}
export function postrating (query) {
	return request({
		url: '/api/rating/',
		method:'post',
		data:query
	})

}

export function postnewcollection (data) {
	return request({
		url: '/api/collection/',
		method:'post',
		data:data
	})
}
