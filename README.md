# PhytoBacExplorer
Code associated with PhytoBacExplorer BBR project (BB/W018853/1)


## A database of taxa that are in scope for the project
We need a database of bacterial taxa that are within scope of this project. I assembled a list of taxonomic names, taken from the following sources:
- Bull, C. T., De Boer, S. H., Denny, T. P., Firrao, G., Saux, M. F.-L., Saddler, G. S., Scortichini, M., Stead, D. E., & Takikawa, Y. (2010). COMPREHENSIVE LIST OF NAMES OF PLANT PATHOGENIC BACTERIA, 1980-2007. Journal of Plant Pathology, 92(3), 551–592. http://www.jstor.org/stable/41998846
- https://lpsn.dsmz.de/genus/xanthomonas
- Bull, C. T., De Boer, S. H., Denny, T. P., Firrao, G., Fischer-Le Saux, M., Saddler, G. S., Scortichini, M., Stead, D. E., & Takikawa, Y. (2012). LIST OF NEW NAMES OF PLANT PATHOGENIC BACTERIA (2008-2010) Prepared by the International Society of Plant Pathology Committee on the Taxonomy of Plant Pathogenic Bacteria (ISPP-CTPPB). Journal of Plant Pathology, 94(1), 21–27. http://www.jstor.org/stable/45156005.

I downloaded the following file from the NCBI Taxonomy database: https://ftp.ncbi.nih.gov/pub/taxonomy/taxdump.tar.gz. This tarball contains the file ```names.dmp``` from which I was able to extract the taxIDs via the script ```get_taxids_for_named_taxa.py```. By executing ```python get_taxids_for_named_taxa.py > names_and_ids.txt``` I was able to get a tab-delimited table of taxonomic names and their taxIDs. This could then be subsequently edited manually.


