def paginate(query, page, per_page):
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
