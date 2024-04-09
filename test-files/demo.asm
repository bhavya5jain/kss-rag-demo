         TITLE 'RAG DEMO'
         ENTRY DEMO
DEMO     CSECT
         L     1,=F'123'
         L     2,=F'456'
         AR    1,2
         WTO   'Calculation complete'
         END   DEMO
