Redact an Org file by replacing heading titles, body text and property values by random words from an input file.

Uses [orgmunge][1] to read an Org file and write a redacted version of it, where all important info (heading titles, body content, metadata, and property values) are replaced by random words from a file.
You can generate a file of Lorem Ipsum text using, for example, [this page][2].

Usage:
redactOrg /path/to/lipsum.txt /path/to/input_file.org /path/to_output_file.org


  [1]: https://github.com/durableOne/orgmunge
  [2]: https://www.lipsum.com/
