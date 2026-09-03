# Claim NNN: <!-- title: the statement in one line -->

*Created D Month YYYY; updated D Month YYYY.*
Register: OPEN
Kind: <!-- formal | computational | empirical | inferential | documentary | interpretive | internal-consistency -->
Verdict: none
Plan: NNN, task M
Verified-by: unchecked

<!-- HEADER FIELDS. One per line: name, colon, value, nothing after the
     value. Delete these comments in the instance.
     Register     VERIFIED | DERIVED | ATTESTED | SPECULATIVE | RULED_OUT |
                  OPEN. A new claim starts at OPEN; the researcher assigns
                  the rest (CHECK_METHODOLOGY.md section 1).
     Kind         one of the seven above (CHECK_METHODOLOGY.md section 2).
     Verdict      none while OPEN or SPECULATIVE; otherwise, by kind:
                  formal: proved | disproved
                  computational: reproduced | not reproduced
                  empirical: compatible | in tension | refuted
                  inferential: identified as stated | assumption unsupported,
                    and replicated | not replicated (two values, comma-separated)
                  documentary: confirmed | not confirmed
                  interpretive: supported | underdetermined | contradicted
                  internal-consistency: consistent | inconsistent
     Plan         the owning plan under research_plans/, task optional. A
                  claim needs one; open a plan first.
     Verified-by  researcher | assistant, <route> | deferred, <instrument> |
                  unchecked | <party from the roster {{PARTIES}}, ONTOLOGY.md
                  Slots>, <route>
     Add these lines when they apply, and not before:
     Backed-by: [check NNN]      once a check exists; mandatory once the
                                 register is VERIFIED or RULED_OUT
     Depends-on: NNN, NNN        claims this one rests on
     Frame: <what fixes it>      the units, encoding, edition, sample
                                 definition, or coding the claim's quantities
                                 are stated in, e.g. "the base manuscript's
                                 foliation, fixed in [claim 002]" or "the
                                 2019 sample definition, fixed in [check 004]"
     Original: <pointer>         where the claim has no external source
     Reserved D Month YYYY, plan NNN     a comma, never a colon
     Pre-registered D Month YYYY, <locator> -->

## Claim

<!-- The statement, precisely, with its scope. Every input classified in
     the text as derived, imposed, or conjectured (CHECK_METHODOLOGY.md
     section 4). Cite sources by [ShortKey, locus], the locus a page,
     section, folio, table, or variable as the project fixes in
     {{CITATION_LOCUS}} (ONTOLOGY.md, Slots); cite claims by [claim NNN].
     Split any sentence that would carry two registers. -->

## What is not claimed

<!-- The scope fence: what a reader might take this claim to say that it
     does not. The adjacent question deferred to another plan, the
     generalization not made, the source not consulted. Part of the claim
     (PRECEDENCE.md, "tier 1 does not inflate"). -->

## Evidence and route

<!-- Empty while OPEN. Then: how the claim was reached; for an empirical
     or inferential claim, what it was compared with and the range of
     independent determinations; and a pointer to the check, which
     records the second pass. Do not repeat the check here. -->

## References

<!-- Every [ShortKey] cited above, each registered under
     evidence_and_reasoning/references/. -->
