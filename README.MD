# ShrekBOT 3000
It's a silly discord bot that spits out random text with Markov chain model fit on Shrek movie script.

The pre-fit matrix is stored as `matrix/shrek.pkl`, which does NOT contain the original movie script. It's just a matrix of words with corresponding probabilities. This entire repository does NOT contain any copyrighted material. Please don't sue me.

That said, script used to fit the probability matrix was obtained from [here](https://gist.github.com/liamhendricks/5f8342659ff341b9dc4f328bca7be7da). Thanks [@liamhendricks](https://gist.github.com/liamhendricks). You can place that .txt file in `data/` and build your own matrix from scratch, if you so desire. Or with any other movie script/corpus. Just make sure to write your own text processing function so that data will be formatted correctly for matrix builder.
