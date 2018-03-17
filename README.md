# Brewers Association Website Scraper

## Purpose and Goal

I created this scraper so that I could obtain the names, locations, types and websites for all of the breweries in the United States registered with the Brewers Association. After scraping that information, I wanted to go to each website and take a screenshot of the homepage. These images would allow me to conduct several analyses about brewery branding. Also, I intend to use the location data to examine where breweries are most densely populated and hopefully to create interactive maps.

## Steps

The first step in creating this scraper was to write Selenium code that would ex-out of a pop-up and select “United States” in the dropdown menu.

After the HTML with the brewery information was visible to my tester, I was able to start writing my BeautifulSoup code. All of the breweries’ information was contained in separate divs with the class `brewery`. I found all of those and put them in the variable `brewery_boxes`. Then, I created the function `get_info()` to loop through each of the individual brewery divs and extract the information I wanted, mostly using li classes. I assigned a variable to each, such as `name` and `address`. Because some breweries didn’t have a website link available, I had to use a try and except clause. At the end of the function, I plugged the variables into a list and returned the list so that it would eventually be written to my CSV.

The next function I wrote, `get_list`, was necessary to append the urls to a seperate list that would be looped through to obtain the screenshots. I needed to extract the `href`, and this was the only way I could figure out how to successfully do that.

The next section of the code writes the information obtained from `get_info` into a CSV file.

Lastly, I used a for loop to loop through the urls I appended to `url_list`. In the loop, I created a file name that used the date and time to assure that each screenshot would have a unique name, preventing it from overwriting other images. I used `shutil` to immediately move the screenshot from my computer to my external hard drive to conserve space. I used a try and except clause here too so that it didn’t break the code when it hit a variable with no link in it.

## Problems

This was one giant puzzle. It took me a long time to figure out how to make the pieces fit. The first problem I found was the pop-up window. It didn’t appear before I started making this scraper, so it was a challenge figuring my way around it, and additional time spent writing Selenium.

After I figured out all of the Selenium, the scraper still couldn’t access the internal HTML. Luckily, Professor McAdams so graciously helped me with this issue, but I spent a lot of time grappling with it myself.

For some reason it was particularly difficult to get the `href`. It took me a really long time to figure out, but eventually writing a seperate function did the trick.

When I started trying to take the screenshots, I realized immediately that I was going to need to find a way to give them all unique names. This took me a decent amount of thought, but I figured something out that worked.

Besides those problems, I mostly just ran into standard coding issues -- figuring out what was causing the error messages and playing around until I fixed it.
