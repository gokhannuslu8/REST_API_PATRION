def paginate(query, page, per_page):
    """
       Paginates the results of a query based on the specified page and per-page parameters.

       This method takes a query object and returns a subset of results for the specified
       page number, with the number of results per page defined by `per_page`. It calculates
       the correct subset of results to return based on the page and per-page values.
       """
    page = int(page)
    per_page = int(per_page)
    total = query.count()
    items = query.skip((page - 1) * per_page).limit(per_page)
    return {
        'items': list(items),
        'total': total,
        'page': page,
        'per_page': per_page
    }
