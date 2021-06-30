# Crawl Data from https://a1.marugotoweb.jp/en/hiragana.php
library(rvest)
library(dplyr)

url = "https://a1.marugotoweb.jp/en/hiragana.php"
html = read_html(url)

# Get char img
form_img <- html %>% 
    html_nodes('img[src*="images/hiragana/form"]') %>%
    html_attr("src") %>%
    paste0("https://a1.marugotoweb.jp/en/", .)
form_img_local <- sapply(form_img, function(url) {
    local <- file.path("hiragana/img", basename(url))
    download.file(url, local)
    return(local)
})

# Get audio
audio <- html %>% 
    html_nodes('source[src*="sounds/common/"]') %>%
    html_attr("src") %>%
    paste0("https://a1.marugotoweb.jp/en/", .)
audio_local <- sapply(audio, function(url) {
    local <- file.path("hiragana/audio", basename(url))
    download.file(url, local)
    return(local)
})


# Get char form
form_text <- html %>% 
    html_nodes('img[src*="images/hiragana/form"]') %>%
    html_attr("alt") 


# Combine data
d <- tibble(
    form = form_text,
    roman = basename(form_img) %>% gsub(".png", "", ., fixed = T),
    img = form_img_local,
    audio = audio_local
)
writeLines(jsonlite::toJSON(d), "hiragana.json")

