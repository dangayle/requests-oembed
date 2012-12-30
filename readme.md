# Requests oEmbed

A library to embed html objects via oEmbed, using the [Requests](https://github.com/kennethreitz/requests) lib.

## usage

    from requests_oembed import get_embed_html

    print get_embed_html('https://twitter.com/dangayle/status/284836686171627521')

    # <blockquote class="twitter-tweet"><p>Coding a <a href="https://twitter.com/search/%23python">#python</a> script using @<a href="https://twitter.com/kennethreitz">kennethreitz</a>' Requests so I can convert WordPress posts with oEmbedded objects into static html</p>&mdash; Dan Gayle (@dangayle) <a href="https://twitter.com/dangayle/status/284836686171627521" data-datetime="2012-12-29T01:42:12+00:00">December 29, 2012</a></blockquote>
    # <script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>