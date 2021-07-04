# Crawl data from https://a1.marugotoweb.jp/en/hiragana.php
library(rvest)
library(dplyr)

url = "https://a1.marugotoweb.jp/en/hiragana.php"
html1 = read_html(url)

# Get char img
form_img <- html1 %>% 
    html_nodes('img[src*="images/hiragana/form"]') %>%
    html_attr("src") %>%
    paste0("https://a1.marugotoweb.jp/en/", .)
# form_img_local <- sapply(form_img, function(url) {
#     local <- file.path("hiragana/img", basename(url))
#     download.file(url, local)
#     return(local)
# })

# Get audio
audio <- html1 %>% 
    html_nodes('source[src*="sounds/common/"]') %>%
    html_attr("src") %>%
    paste0("https://a1.marugotoweb.jp/en/", .)
# audio_local <- sapply(audio, function(url) {
#     local <- file.path("hiragana/audio", basename(url))
#     download.file(url, local)
#     return(local)
# })


# Get char form
hiragana <- html1 %>% 
    html_nodes('img[src*="images/hiragana/form"]') %>%
    html_attr("alt") 


# Crawl data from https://a1.marugotoweb.jp/en/katakana.php
url = "https://a1.marugotoweb.jp/en/katakana.php"
html2 = read_html(url)
# Get char img
form_img <- html2 %>% 
    html_nodes('img[src*="images/katakana/form"]') %>%
    html_attr("src") %>%
    paste0("https://a1.marugotoweb.jp/en/", .)
# form_img_local <- sapply(form_img, function(url) {
#     local <- file.path("data/katakana", basename(url))
#     download.file(url, local)
#     return(local)
# })

katakana <- html2 %>% 
    html_nodes('img[src*="images/katakana/form"]') %>%
    html_attr("alt") 


# Combine data
d <- tibble(
    hiragana = hiragana,
    katakana = katakana,
    roman = basename(form_img) %>% gsub(".png", "", ., fixed = T),
    audio = paste0(roman, ".mp3"),
    img_hira = file.path("data/hiragana", basename(form_img)),
    img_kata = file.path("data/katakana", basename(form_img))
)
writeLines(jsonlite::toJSON(d, pretty = T), "gojuon.json")
