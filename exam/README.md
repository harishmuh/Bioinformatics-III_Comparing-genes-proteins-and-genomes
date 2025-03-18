# Bioinformatics III Application Challenge (Week 6)

## Instructions
In this Application Challenge, we are going to hop in the Bioinformatics Time Machine and head back to 1996.

Pretend  that you are working with Mohamed Marahiel to discover the  non-ribosomal code by determining the structural components of  gramicidin synthetase, a protein that makes the non-ribosomal peptide  gramicidin. You know that it has an adenylation domain (A-domain), but  you do not know where it is located in the sequence of amino acids  making up the protein.

Fortunately, Peter Brick just published the  3-D structure of firefly luciferase, which has similarities to  A-domains. You think that this information might be useful in finding  the A-domain of gramicidin synthetase, and so you obtain the amino acid  sequence of gramicidin synthetase, which you decide to compare against  the much shorter sequence for firefly luciferase to locate the A-domain  in the gramicidin synthetase sequence.

Throughout this challenge, you will need two datasets [(in FASTA format)](https://en.wikipedia.org/wiki/FASTA_format)

the amino acid sequence of gramicidin synthetase [(grs.fa)](https://bioinformaticsalgorithms.com/data/challengedatasets/grs.txt)

the amino acid sequence of firefly luciferase [(firefly_luc.fa)](https://bioinformaticsalgorithms.com/data/challengedatasets/grs.txt)

First, let's check whether gramicidin synthetase is similar to firefly luciferase. To this end, we could run a local alignment algorithm that we encountered in the main text. But what we would like to do is align gramicidin synthetase against all firefly proteins to see if firefly luciferase really is the most similar to gramicidin synthetase. Unfortunately, such a task is computationally very intensive -- especially in 1996!
Instead, we will use a heuristic called **BLAST** (the **B**asic **L**ocal **A**lignment **S**earch **T**ool) that does not guarantee an optimal alignment, but which quickly returns a measure of similarity hits of a sequence against a database. BLAST was published in 1990 in one of [the most cited](https://pubmed.ncbi.nlm.nih.gov/2231712/) scientific papers of all time.

In general, if we are searching a protein against a database and find a hit with score S, then the **E-value** of S is the expected number of hits in searches of this protein against a random database of the same size. Thus, the smaller the E-value, the less likely that the hit resulted from random noise, and the more statistically significant the result.
For a given match of two sequences, the **percent identity** corresponds to the percentage of residues that are identical in the two sequences at the same positions in the alignment.

Run only the gramicidin synthetase sequence [(grs.fa)](https://bioinformaticsalgorithms.com/data/challengedatasets/grs.txt) on BLASTp, the version of BLAST used for aligning an amino acid sequence against a database of proteins: 

[http://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome](http://blast.ncbi.nlm.nih.gov/Blast.cgi?PROGRAM=blastp&PAGE_TYPE=BlastSearch&LINK_LOC=blasthome)

Use the non-redundant protein database, and specify the organism to be the “North American firefly (taxid: 7054)”; otherwise, use default parameters.

* **Consult the "descriptions" section and report the E-value and the percent identity of the best match.**
  
  **Answer**: The best match is 'uncharacterized protein LOC116175982 [Photinus pyralis]' with E-value: 3e-57 and percent identity 28.55%. The results originates from firefly (Photinus pyralis) as well, but not luciferase. The e value of 3e-57 considered as statistically significant.

* **Was firefly luciferase identified as a statistically significant match? Explain your answer.**
  
  **Answer**: The result: luciferase [Photninus pyralis] got 8e-14 with percent identity 21.80%. Yes, this is statistically significant because 8e-14 is still a very low E-value, meaning the match is unlikely to have occurred by chance. Typically, E-values < 1e-5 are considered statistically significant in bioinformatics. However, this firefly luciferase is not the best match.
  
* **Consult the "alignments" section. According to the first alignment, report the start and end index of the putative A-domain of the gramicidin synthetase sequence.**

  **Answer**:
  The A-domain (Adenylation domain) is part of non-ribosomal peptide synthetases (NRPSs) that selects and activates specific amino acids.
  In bacterial NRPS enzymes like Gramicidin Synthetase, A-domains typically contain conserved sequence motifs such as:
  * A3 (core motif): "GEGL"
  * A5 (core motif): "YTSG"
  
  Based on my result the "GEGL" appears at position 381-384. This strongly indicates the A-domain starts before this position. While 'YTSG' YTSG" appears at position 189-192. This is another core motif of the A-domain.
  Based on motif positions, the putative A-domain in the Query sequence likely starts before position 189 and ends around position 384.

  Final Answer:
  * Start index: ~189
  * End index: ~384
  These positions mark the likely region containing the A-domain in the gramicidin synthetase sequence.

Now that we have examined the statistical significance of the protein match, we will align gramicidin synthetase (grs.fa) with firefly luciferase (firefly_luc.fa).

In particular, we will use EMBOSS to perform a global and local alignment of the two sequences.
* **EMBOSS Needle (Global alignment)**: [http://www.ebi.ac.uk/Tools/psa/emboss_needle/](http://www.ebi.ac.uk/Tools/psa/emboss_needle/) 
* **EMBOSS Water (Local alignment)**: [http://www.ebi.ac.uk/Tools/psa/emboss_water/](http://www.ebi.ac.uk/Tools/psa/emboss_water/)

In both cases, click on "More Options" and select the **PAM150 scoring matrix**; otherwise, use default parameters.

* **Is global alignment or local alignment more appropriate in this case? Give a short explanation that includes a comparison of the percent identity and total score of each alignment.**

  **Answer**:

  Based on the results, local alignment (EMBOSS Water) is more appropriate in this case. Here’s why:

  **Global Alignment (Emboss Needle) report:**
  * Percent Identity: 10.3% (122/1179)
  * Similarity: 22.3%
  * Gaps: 60.2%
  * Score: 152.0
  This method forces an alignment over the entire length of both sequences, which introduces many gaps and lowers the overall identity because the sequences only share a similar region.

  **Local Alignment (Emboss Water) report:**
  * Percent Identity: 21.3% (111/521)
  * Similarity: 44.9%
  * Gaps: 19.4%
  * Score: 171.0
  This approach finds the best matching region between the two sequences, resulting in a much higher percent identity and similarity with far fewer gaps.
  
  Conclusion:
  
  So, Local alignment is more appropriate here because it isolates the region where the two proteins actually share significant similarity, whereas global alignment dilutes the similarity by forcing an alignment across the entire sequence length—even regions that are not homologous.

* **What do each of these alignments suggest is the A-domain of gramicidin? Report the start and end index of the putative A-domain for each alignment. How do these values compare with what BLAST reported?**

  **Answer**:

  Let's break down the results based on the alignment
  
  **EMBOSS Water (Local Alignment)**
  * Aligned Query Region: The local alignment starts at residue 67 and ends at residue 525 in gramicidin synthetase.
  * Interpretation: Because local alignment extracts only the best-matching segment, this 67–525 region (a span of 459 amino acids) is proposed as the putative A-domain. It shows a relatively high percent identity (21.3%) and similarity (44.9%) with fewer gaps (19.4%), suggesting that this continuous segment is functionally and evolutionarily conserved.

  **EMBOSS Needle (Global Alignment)**
  
  * Aligned Query Region: The global alignment forces an end-to-end comparison, and although it covers the entire gramicidin synthetase sequence (positions 1–1179), the significant alignment with firefly luciferase is confined to the first 525 residues.
  * Interpretation: While the global alignment formally spans residues 1–525, the region contributing most to the similarity appears to be from around residue 67 to 525—matching the region identified by the local alignment. The initial segment (residues 1–66) aligns with only weak similarity and likely does not contribute to the core domain.

  **Comparison with BLAST**
  * BLAST Report: Earlier BLAST results highlighted the best match (with an uncharacterized firefly protein) and provided an estimated A-domain region roughly in the range of ~189 to ~384.
  * Discrepancy: The EMBOSS alignments suggest a broader region (approximately 67 to 525) is homologous to firefly luciferase.
  * Reason: BLAST often focuses on the most statistically robust core of similarity, whereas EMBOSS Water (and to a lesser extent the Needle global alignment) recovers an extended region of conservation. This may indicate that the functional A-domain is larger than the BLAST “core” region, or that the additional flanking residues contribute to the overall structure and function of the domain.

  **Final answer**
  * Local Alignment (EMBOSS Water): Putative A-domain from residue 67 to 525.
  * Global Alignment (EMBOSS Needle): Indicates that the only significant similarity lies in the first 525 residues, with the core of the match being roughly 67–525.
  * Comparison with BLAST: The EMBOSS-derived region is broader than BLAST’s estimated ~189–384, suggesting that the A-domain might extend further than what the BLAST core alignment indicated.
  These observations imply that the conserved, functionally relevant A-domain of gramicidin synthetase likely spans from about residue 67 to 525, encompassing a larger area than the core region identified by BLAST alone.

Rerun EMBOSS Water (but not EMBOSS Needle) with the following parameter values for an alignment with affine gap penalties (continue using PAM150): 
    * GAP OPEN = 20, GAP EXTEND = 0.2
    * GAP OPEN = 5, GAP EXTEND = 1.0

* **How do these alignments compare with the local alignment that you generated using the default parameters? Which of the three alignments is likely to be the most biologically relevant in this case? Explain your answer.**

  **Answer**:
  
  Summary of the Three Alignments:

  **Default EMBOSS Water (Default gap penalties: gap open = 10, gap extend = 0.5)**
  * Length: 521 residues
  * Identity: 111/521 (21.3%)
  * Score: 171.0
  * Interpretation: This alignment identifies a moderately long region of similarity between the two proteins. It likely captures a conserved domain (such as the A-domain) but may not extend to its full boundaries.

  **Alignment with Gap Open = 20, Gap Extend = 0.2**
  * Length: 103 residues
  * Identity: 30/103 (29.1%)
  * Score: 91.6
  * Interpretation: With a high gap‐opening penalty and a very low extension penalty, the algorithm “prefers” to have a single, tight block of alignment. The resulting alignment is short but has a higher percent identity within that block. However, it covers only a small core region and may miss additional biologically relevant residues that belong to the conserved domain.

  **Alignment with Gap Open = 5, Gap Extend = 1.0**
  * Length: 595 residues
  * Identity: 153/595 (25.7%)
  * Score: 309.0
  * Interpretation: A lower gap‐opening penalty combined with a higher extension penalty allows the algorithm to insert gaps more liberally at the beginning while still penalizing extended gaps. The result is a longer alignment that covers a broader region of similarity. The overall score is higher, suggesting that more of the domain (or surrounding homologous regions) is being captured.

  **Comparison and Biological Relevance**
  * Short vs. Long Alignments:
    * The 103-residue alignment (high gap open, low gap extend) focuses on a very high-quality local match (higher percent identity) but is too short to represent the entire functional domain.
    * The 595-residue alignment (low gap open, high gap extend) captures a longer region that likely includes additional parts of the domain or adjacent conserved regions.
  * Score and Coverage:
    * The default alignment (521 residues) and the 595-residue alignment both cover a region comparable in length to known domains (e.g., adenylation domains are typically several hundred residues long).
    * The second result (595 residues, score = 309.0) has a higher score and slightly higher percent identity than the default, indicating that it may be recovering a more complete or functionally relevant region.
  * Biological Relevance:
    * A biologically relevant alignment should capture as much of the functional, conserved region as possible without including an extraneous sequence that isn’t homologous.
    * Although the 103-residue alignment shows a higher percent identity (29.1%), its short length suggests it might only represent the core of the domain, missing flanking regions that contribute to the domain’s structure and function.
    * The 595-residue alignment appears to recover a more extended region of similarity (with a good percent identity of 25.7% and a high score), implying that it might correspond more closely to the entire conserved domain found in gramicidin synthetase.
    
  **So, Among the three**
  * The alignment with gap open = 5 and gap extend = 1.0 (595 residues, score = 309.0) is most likely to be biologically relevant.
  * This alignment covers a longer and more comprehensive region of similarity, which is consistent with the expected size of a functional domain, even though its percent identity is slightly lower than the very short (103-residue) alignment. The default alignment (521 residues) is in a similar range, but the second alignment’s higher overall score suggests it may better capture the full extent of homologous, functionally conserved regions.
  * Thus, the second alignment (with gap open = 5, gap extend = 1.0) provides the most biologically meaningful view of the conserved region between gramicidin synthetase and firefly luciferase.


Now that we have verified the similarity of gramicidin synthetase to firefly luciferase, we would like to construct a multiple-sequence alignment between the gramicidin synthetase sequence and other known A-domains.

For this task, we will use an extremely popular program called Clustal Omega. We will examine PheA, which corresponds to a segment of gramicidin synthetase that codes for phenylalanine.

Run Clustal Omega [(http://www.ebi.ac.uk/Tools/msa/clustalo/)](http://www.ebi.ac.uk/Tools/msa/clustalo/) on [a_domains.fa](https://bioinformaticsalgorithms.com/data/challengedatasets/a_domains.txt), which includes PheA as well as the A-domains of eight other non-ribosomal peptide synthetases from various bacteria. Use default parameters with the Output Format “Clustal w/ Numbers.” Examine the resulting output (use the Show Colors button and the Result Summary tab).

* **Upload a snapshot of the phylogenetic tree and the percent identity matrix generated for this alignment as an image file.**

![Percent identity and phylogenetic tree](https://github.com/harishmuh/Bioinformatics-III_Comparing-genes-proteins-and-genomes/blob/main/exam/Percent%20identity%20matrix_Phylogenetic%20tree.PNG?raw=true)



Marahiel determined a handful amino acid positions that are responsible for determining the amino acid that binds to the A-domain. Five of those amino acids correspond to positions 236, 239, 278, 299, and 301 of the PheA sequence.

* **Consult the multiple sequence alignment produced by Clustal Omega. Based on the positions reported by Marahiel, do the A-domain sequences appear to code for the same amino acid? Explain your answer.**

  **Answer**: 

  Marahiel identified five key positions (236, 239, 278, 299, and 301 in PheA) that influence which amino acid is activated by the A-domain. When we look at these positions in the Clustal Omega alignment, we notice that the amino acids at these spots are not the same across all the sequences. This explains that these positions of Phea are poorly conserved.

  The remaining residues appear in a window from positions 320 – 332 of the PheA sequence which are reproduced below (with gaps represented by the symbol X):

  | Amino acid residues | Position | Sequence        | Position |
  |------|--------|----------------|--------|
  | Ite  | 323    | VNVYGPTEVTIGCS  | 336    |
  | Yp5  | 724    | FNTYGPTEATVVAT  | 737    |
  | Abw  | 755    | INAYGPSEAHXLVS  | 767    |
  | Dhv  | 291    | MNTYGPTEATVAVT  | 304    |
  | Yp0  | 793    | INEYGPTETTVGCT  | 806    |
  | Np7  | 755    | VNVYGPTEATGHCL  | 758    |
  | Vsq  | 750    | INCYGPTEGTXVFA  | 762    |
  | PheA | 320    | INAYGPTETTXICA  | 332    |
  | Aap  | 659    | VNNYGPTETTXVVA  | 671    |

Can you locate the positions in this window that are responsible for determining the amino acid that binds to the A-domain?

* **Report your top three candidates as positions in the PheA sequence. (Hint: Construct a sequence logo from these sequences as a starting point via WebLogo –** [http://weblogo.threeplusone.com/](http://weblogo.threeplusone.com/)**.) Why did you choose these candidates?**

  **Answer**:

  ![Phea sequence weblogo](https://github.com/harishmuh/Bioinformatics-III_Comparing-genes-proteins-and-genomes/blob/main/exam/Phenylalanine_sequence_weblogo_generated.png?raw=true)
  
  Within this 320–332 window, we can distinguish two parts:

  * A Conserved Core (GPTE):
  In nearly every sequence the central “GPTE” motif is maintained. This conservation suggests that these residues are important for the overall structure of the A-domain rather than for determining substrate specificity.

  * Flanking Residues:
  The residues immediately before and after the GPTE motif (in PheA, “INAY” at positions 320–323 and the following residues “TTXICA” at positions 328–332) show noticeable variation among the different A-domain sequences. This variability is key; these flanking positions are where differences occur that correlate with the binding of different amino acids.

  Conclusion:

  The positions in the window that are likely responsible for determining which amino acid binds to the A-domain are those outside the invariant GPTE core—in other words, the variable residues flanking the GPTE motif (positions 320–323 and 328–332 in PheA).



* **Some positions in the multiple alignments show very high conservation between all sequences. What is a possible biological interpretation for this conservation?**

  **Answer**:
  
  Highly conserved positions across the sequences usually indicate that these residues play crucial roles in the protein's function or structure. In this case, the conservation suggests that these amino acids are important for:
  * Catalytic Activity: They might be directly involved in the chemical reaction that the A-domain catalyzes.
  * Substrate Binding: They could be essential for binding the specific amino acid or intermediate.
  * Structural Stability: They may help maintain the proper 3D structure of the A-domain, ensuring it folds correctly and remains stable.
  Because any changes in these conserved residues could disrupt the enzyme's function or structure (including homology), they are maintained throughout evolution.
