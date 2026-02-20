blog_views = [150, 800, 2500, 600, 1200, 450, 3000]

post_count = 0
count = 0
print("")
for i in blog_views:
    if i > 1000:
        count += i
        post_count += 1
        print(f"Views: {i} - Trending")
    elif 500 < i < 1000:
        count += i
        print(f"Views: {i} - Average") 
    else:
        count += i
        print(f"Views: {i} - Low traffic")

print(f"\nTotal number of views: {count}")
print(f"Trending posts: {post_count}\n")        
