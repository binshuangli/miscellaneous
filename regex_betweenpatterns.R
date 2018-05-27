s <- "PRODUCT colgate good but not goodOKAY"
sub(".*PRODUCT *(.*?) *OKAY.*", "\\1", s)
#giving "colgate good but not good"
