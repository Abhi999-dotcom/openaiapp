import streamlit as st
st.image("data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQABAAD/2wCEAAkGBxMTEhUTEhMVFRUXGBcVFxYXFhcaGBcYFRcWFxgXGBYYHSggGholGxUWITEhJSkrLi4uGB8zODMsOCgtLisBCgoKDg0OGxAQGy0mICUtLS0tLS0tLy0tLS0tLS0tLS0tLS0tLy0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLf/AABEIAKgBLAMBEQACEQEDEQH/xAAbAAACAwEBAQAAAAAAAAAAAAAEBQECAwYAB//EAEEQAAIBAwIEBAMFCAEDAgcBAAECEQADIQQSBTFBURMiYXEGMoFCUpGhsRQjM2LB0eHwkkNyglPxFSREg5Oi0gf/xAAaAQADAQEBAQAAAAAAAAAAAAABAgMABAUG/8QAOREAAQMCAwUHAwIFBQEBAAAAAQACEQMhEjFBBFFhcfATIoGRobHBMtHhQvEFFCNSYjNyorLCkiT/2gAMAwEAAhEDEQA/APj26uiEVG+tCyjdRhZRNMAspowspowspFGFlYUQirinAJRVhTxKKItCqCITBbKtCNyYIi2lHDCZb27dHCAEQvXLdTITFG8G0bOxCicGmaN6EwqXrUMwNNZC6HZKyELO3ZlqMSkNkbqrcACnGSUGUCLVMBZAq4sYopSRKkW6IWJUeHRlIbLN7cUUAQh2t1oRmyxZaBMLBeFutErArzLFbCBmjMrBxU43Iqm2gAViir3DHVN5Ais6jF0A4FBEVIwiqmlIKyqaUjRZRUzZZQaUrKKWFlnNTQU0VlIrQipFEBZSKcLKwFPgWU0YiyykVohFXFUaNFldabBCYImwKo0Sjki0SjBlPZFWrdYhMFvbTNKmAV79vFByy14bqTbmJk4xQEDNcu0B5jCrOhySMnvRV2ThErFkxTtWcp0OnlqCRxsiNcgpgpiUKtkzyppWkQtWsVlPEFDJiKKWSqsmMUUs3usGt04QJvZCPboKklZi3WzWNl42qN1gQqMk1olGYQ7pSmyIVVWDSkFY5JhqtcCkUpqaLkp0SHSSk7UvJdqoaQSsqmploCyikESsoNK4LKtLhWVKkgpooqaaEF4UQipphwWVhTgFZWApwEVYCmACy0t2yeQJ9qfszNkQrhaxBTBEWhRCYJjZWapmjki7VqlhMDuRlu12oI31Xr1uaVGwU6Jdst2zQdCRxOGyKu6832JaMADAigMOilSc4i6G1FqmVAUVotMYmMd6BKmSFTUWs8qYJZlVt26aVN0Bafs5rAqZcFR7QPLnRlKCQsmt+lGUNENds9qZEHeh2s0U0qXs4xTZJGuk3WTWu9BPO5YvZiijilYMlYIlDuhoQSU0iFg60paiCsmFIeCZUIpXNkWQVSKi5qKrQIELIzh2jFwnc20DrWpsxIFwGaFvWoJFSc2DC0ysAKiippgsvRTBqykUwasrCmhZSBVMNrLK4pw0LKwFVgaIp78Pajw5IifWi04TcqFao5v0oPVGXJPU9KDYNyrsJIurW1oyqAI/TqaJlMIhMrNuaUmUBbJGrb5RUyU44q92xIxQlaYzXuGafJ696DlnGbIk6YCSoEdqAU50Qty2SfSmlGwRNnWXFHggeRjJMUkCZXM4vxWyWlzTNzKnb0MGPxp8WixGqyW10oylO9WfTnrWU8Y0WfhAc+dNKUknJUZJpgkNlh+zmiCmLgqNYFGUJKya30AoyiOKzfT4rI4roW4ketMmF0LdSKKYXQzp3rA703JDvaihh3oh05IdxSEgJ1podBcvPstrLdqQy5FZ6/RPZcpcEMKRzIWQtTMDJZbWdQV5Uhe4ZJXMBzWbuSZrAE3RyWLLBioQJRXqN1l6qQSgpFOICysKoASZCysBVGsOaysBTht7IrVBVBwCyItpSPZizWgFdL8I8P0lxyNS5XqOx9zQJwDC1DEAVvxi3pbV/wD+WO9YyCOR9KUP0KxeXN7uayGlkBxyP5U5S0618LrFNOFaFXDS4UgSAetRcYXUTayLsWhHb1NApXEhGabTpclZEnkw5e1TLiLo4gAsuH22s3SHHuO/qKzu8LLE2sj9Vw+fNZBYHmBkg+1IHxYpLnNLG0zgkEEEcxERVJsgYCIvWWW2SCAelDNRe+Lpnxb4mvtpVTw7WdqkgZPr6UjdmDXYpXMzai50QlqpHMVUFO8blk+n9cd6aUuKyxuW6MrSs2HSmlLCldLPOtKUvAyWZsgc+dEFYknJVFiTiAaMrAaFCNbNMCmMRCFu2gc/lTIgkWQtwDtitKcAod7NZOCAhL6RR5oi9wgri0rhATgyjODagW2JmD0NSaQHXUdoDiO6seM6gO0ySe9Zxa42TUA4N7yWRU3GSrqCKi+SVlaKo0CEFjcaSTXOsFFONyy9FENvdZWFWYJWVhVATosrAVQMK0rRRTi2Sy3tinyyQzzRtm2a10ZCJtalV8rY6zXOajWPhwUKzHOMhFcO1FprjCCZHzdvag2qHvNkop1A2Wm40T7h1oIxR/lb5W6UzyQnGCuycnDzCNu8N8M+n6f4qZIIkJqVd04H5+6cXrunfTqS6i7OzbtOfc1zgPxZWVDWaDmjdB8LX3tB0CgRK5+b8Km6u0GE4cAbLWzpBeG24Nl1enX/ADQJw3GSJdGSz0T39NflCqgiGDEQexg/rVRQ7ZuS8rbP4lT2d2EuE7uvlYcT1o8UvfO4tn7qqoMdMnka7KOw903Xlv8A43VfAotHGb+UflDX+N2Cq7kVbZEZBz8pmYBIMkDOSD6TQbJTAN1J+2beXYmnw/cdQVrb4imQGBVQp2E7DtaCIGDkPMxI58qphYBA+688UNqLgXT571Dau3uZXyBHnAUCSJHWMgGO/rFQdRYcrFenR2raw3ERI61srNpkmMgZ8xgrzgeYHrHapmiRkfDIrop/xIOnG0gjOLgfKG1GhK5IlehHL8RU7ixXbTrMqtmm4FDC2OoijKYyF5rB/wA1pQxCFndUHBOaaUotcIS8gIiPrRlOh7to9qYI4gEK9n8ewoohxOQTH4a+Hhq7pt+KttlyVb5iO4FSqVxTvCqGE5of4j4J+zXjbW4twRMqRI9wOVPSq4xKLmhq5rWWcVSEwclZ50uJUhUcUrr2WCyuIYkjHegWQEwWQFJAGaKbcI+HL+pBa0oKjBJIAntS4S68rQgNXo3tuUdSGGCKIaVigBUoGSCmKbCcllYCqYDkVpUgU4aAsrAVZonJBXVaZoKxWqrTQsm3DND4gJBG5c7OrDrFZzgChhJGd0fe0AADplTznmp7Gi4blz0doJcab/qHqsLmjVonPtUalNrs11AkpvwvRhSLYSd/KBLT6Uoa1gXM8Od32G40TO9orllvCvowByJHKeorB4cLFYjF/Up2dqN6d8OjaEcyvR+3v6VF7S24Sdu2v3XWdolOr4LeS7O792G3R/vSlkkWNk9KMcVPq91bg/GXWy9pb11RJ2qh5k+p5Ch2TTeAud9ZzXQZTzSal9PaTx1m6oDHmWXcCRu+gnP9avR2UVjMwFx7Z/EqlMdnREnUnSd3FKdfx1CGN2eQKOOWflWRGcHJP2T9fQIbSgA814tPZX1L68fDh68skmXjjXDstsGIwu5csGxu2KDynIktkRMGJMrtcS0+/XwvTH8OFI9oOs0bd4Ou0m++3auzYNjMAWZiBGJlo3TPMZjADbkDI3lA7TIaWCXTpYWm5OUInRX9L5LdlIbCq7Krk74x5uRluw6dqLWtHecbeIXO87WQRGpsFve1jSWD71LlQSCWU8hG5RsJhRy/tT4WQCQFKHmadxnYk368FOgth/4jC6Ax2Fp3iehCEFZ5SDGfSg9mhF+Cm+s6j3qJiRccudimli+RvW4uzr5pE7QQMZmcZAxSVKYfEX/PFJRquonE0wY9tCOf4Vb+ngSIg84zB7VwPbgdC97ZdoG0MxajMIN1MZGKAVyQDZDeDJjJ7RTSjiJFkQnDG5tCDux/pS9oE2A6rO9ZtDmWuH0wv40QXFH+mwIULcuuLdlArNgARn6mmIDRLimbUmzQl/FOHNpLwXVAozLuDBunXIrMqU3ZJawrZtS60bb3bhtTyGD/AHpw5pPdRp42tHaIPiNqAaddDXSkvWlkBVuoY1sSELoNbxPdpBZ8m0ddo3H60O7hmVztrVO0wkJTwf4bv6kM1lQVHMkgZ7VPDxXYiuGXLlklUZkadriY5UWAZSuWq9zCVvrNcWaTs+oBP41jbVK2s+FxwpQIXWrCqNE2WRGm0+6cxAkDv6CqdnBulLoXrlhlMMpU84YEGD6GqQEV4LTCckFqtvpTRolxRdEW7YowEJJR2kZkIZcEZBFKVo3ruOG8Mu6hDfWw8gfvV2kLcH3lnrXN2rabsJNlPaaJqM7tnDIpVreFbIdDutnkRzHoexqxUdl2ztD2bxDxmPsiuE8f/Zm5LkHaXE7T3B6VCq1r7OKet2lPvUwCTmt31TOxN64bgcAzJO32n9KwaG2AgJKRdUHasPeGY+EyXTtZVTO+032h0Pb0oB98JTVaTNpHaMs4Jvo3DAKcg/Kfuz+oqT2lhxNU2VRVGCpYjVA2OD29L4pWdxMbtrGJ3SFxiYif0rp2emJB33zXh7ftT6zoBIAkWBubpTxBrlwOtsHYcE5MeUMZIxugSV7Tziup9YNtql2TZY73G26UEnC1MtqFEBjKLgnZztp25Ebp6/QcwxVRK9GpVGzgMYJPP1J58PRXt8UAkadERcZtrtbHfvBBxkVdraYMLmOz1HgGqZO45eG5Xuancdt7zgeUODDzOSDALCZmeWBQLxMZJ2bI7DipW4ff4+yDvq9tLTptdLRGy4oG4AySrqIZSWc+Y4yPu5iX4bEdZLqFDtJGROY8r8efgj9tu3bDWS1wXP4tss0Lu5mAx8zLj0gHrAzRmRl6/sM1GsMZDakYxcGLE9dbl9/TXLapcs7trTDqT5wJPLG0qD8snlI504eQcOf2WIp1Wy8RGYOh/O9dFat3bq7oMwAJgFpAgn1hpBxXQS1pzXhwAS09cAttPqXt3UtkbleMyIJgT5hg+YnH96m8NeIdmqg4B2tIxGYnPgUyOmR8qGcyQR0BBgjFec9jmmJgL2qG0teycJJyPXHNeuK6+VVCiJ8v+M0AxpuUHbTUJhvpf1Qj2TBLAt1mMCqQwWKg11erdgPMpffv9linDmjIKg2Z5+tyRcUuONrAkQwIK42nviiTNjkuqm1jLtzSHid5r9wl7jOwxJJP4TUXNYTDbLupOdhlyP4ZowgMTJ51RrcKVzpWPFV6RBp+CamddEjSyScAmlhWc4DMrK9jFYncsL3QzE1MU9U1k24VrQiEK5QnDQSJH0pmOp3lQqGoHWSrUv5pDE9z3rkfBMtyVw2RdZzVW0ZErQAhhVgQLLKwq3eyWTv4U1TWb63E27lyAwkN6RRewwGm0qdSphEpp8X8Yu6tle9sG3ChVAIB7nma1OmKbsMylZUxLn0FdFyiYC3t2Sa0FKXBF2bM+9DNYnCirK5iI6UrltJld5w7431lnTrZXw3KiFuPJIHQEcj71w/yAecWigNrkXF1nwZnvyYD3nJN2yBAcE/Og5AjtTtf2Yh+W9LtOyiuMbLPGR+E04j8JMEVWtAEAm2+D/4XI5HsaiKzS4kGetFalUfgAr2PolPC7nhsbd63uX5SIys9qs7vNsU1Slgd2lPPUb/ynmj0TWlJU+Lp2mVg7gO8dxUXODrOsd6Rzpdip2duOq2TSC0jPbJdGjwzmQTzmOUe451SjLn4XaLzv4nVxUw5mZseEZyk3F9Wd4dmzBGAIHU4iCcr+Nd4IY2Grx6VB1d3e68uvVBLpQtve53QhdUggEmPmj+WMfpUg3E7EvQqbQ9g7Jg1id3XU3SH/wCJve+dRsJaBbVREsSeRwJJzymeeaVtS+EBdY2YMmpN+PLct7vhi4F04J5FhIIAg71MwGMgYGTHtQe/CFfY6VSqZqW3fC7fgXwhdYeJuUMTuCycD0Y8j6j9a4qm0ltivWDaOUW3rHjPA3sRtkDPiLCwQcdxPrNUp1sQsp1tnY9pJz0OvW5c2dGbLi7prodM7hz2AZI2gSwkDv610MGEEDJePXfjOGq2HeUn2+FfS2rqbmS03mYB7RGFfd5pbEDcDBHLI6ZrTIi3NcG1MDjFQ3H6t4v+xC3vWb8BkYMywdm5hMEYZQwmBM5FUce6oU3UcffFtCRn1pwVA72riLdTA2EAQLYaBLicbgRkjBMzGaAvMeao4NeyR5cOPP3XT8AK27TiC8kNCSQZEYByJ2kweUx0rj2ppGErbLUZWqvaRu+2S2v8SuyAluJ+p/LFcoaDqvS7rBcLHU6V/wDrXNo57Tz/AOIrS3RUDqhGUc/slmutgfw5I7t39q6Kc7lyVCzF3n+ASXX21KkOd09BVdIKamTM02xGpS2zojP7u0FH3m/uaZrR+kJ312gf1HzwCPt27ajzPuPZaJZvKUV6r/8ATZbeVovCX1Fu49pbUW/m8RwGmJGDU3VWNIbC6qVCqe89/gFxWtvNMFh7LyHpimJJsumkxgEgHxQN00pkWVwAUM9AjEmFllUHMbmmzXpqeRsivTVASgshV2gNzulVhVQ45LQtbXPBj1rPp9oIlA5Ii0snJJNbZ9nwulxkpHGBZdVoNXZt6C4kTeuMBm2hAUdnPmBpauIVeAUhUk4Qldq1MDrXSbrCBdErajrmgjM6WW9tJ5c/1oFDK2iCGp1AOxQSe4HT3rgDqje6s+jSnEU64Iz2xbd32uHBkHIz0NO1pLIekrktZ/Tsu1t8ZvXryE3zcKgk2p2o/OYURJik7GmyB6rldUqvY45+0JjrdImoUMjhbnSTBx9lh1I6GlM0zBy6yVdkryN4HmOtCieH3HRQtwKGnBnyv6gjke9TIGietD3BzTPWnyENxzaiiIXcw2qIwxU7jI6GVEdyK7NkNr9XsvC/iM1Kjhu+0n45rk9BpjduEXEgLDEFgCRM5ECQZAGBzPY1Z2LFhKvUqMp0Q9hAMR6Wi/QQnEdXdV99pd/oFIBO37wOAFRvQdu2qOj6dFtmosLQKmuc/I4zzhCajSGC9jc6lYEzuUW1CjcM4EDA5REiMoB3O6brsNQY4fla+/8AP31RnDsXAEAkQYbb4owe0AiZiOpGKkAdQJXSx7W3JMekbuvNfTvhnjOxJvEICcCPN+AHIRzrh2iiSYC9MFtQDAgvijX29SoCtt2sDuIBUwQcyPUZ/Kno0HNsg+p2LTImR4r51qrRs3k8O0YQgBmBIJM5JUFSIHWcAnpNd7bEABePUqCoxxe4XPWfwiHALm7ac2rqozhIDqBuYNt+58ztETkdwao1unX50uuB74ADxIyBn36zyWGn1mnO649y4jspDbMoGJZCACsqZ6CQJ+lK0tglqpWp1jhYQDFwdTFxPpdMOHO3hm1dhiQ3gg/MSvKWHKTC8gJOe9VhwE7vZcL20zVllsptYE7t32T74b4jN3YMjYCnmmVCKGtmTzDCfrXPtIlhPWeapRp4KjZzyPll45jcnBvNylV/lQbmz+QrgAheg597+tz5BLbq+GR5SzGPNcJYwMAQOVVHeyhLUOFsvxHmlt5QdzTu7gR9o4AHP8KuABZxXOHVan+kyOJQl7S3Qu5ba21+9cIB/A5phUbk0SqHZznXf4Bc5rrvmIe9vHZBg1Sbd4rop0gP9Kn4lEWGZV8qhQftNE/ieX0rZZBBwDnf1HHkEqujUP4rLZu3EiS6qSsDnLARiomqWkiM8l2jZmwMOQSPUWGWGZWVWmDBgx2J50wABuuu8WQrmcVpC2V1nfsOBLAjpnn+H0pCHFZr2EwCh6mWxYp5UE1J1ll6aoC05rKorqZAMHJKn3wz8J6nXFvACQsbmZgInlgST+FNUeKdneiAjNAavQvZuNauDa6EqwkESOxHMVVlxIQJVraiqCFMkoi0JI9KQsaXYtUqbWtO0AkGG5E4BjGCedaZKBhoRT61WVbfhqGSSXCnc88gWmD+FSbOM3PwsJjKy9bjECKoVgDqjQJjnNKUAMPJU1mm3JEwZx3mpubITyDaFhwzRNbuJdLncmRHIVLsp+pMABMLvNHfGoG5TsurllWIYD7QH6itOHunJebtOz9nNSmPuOI+y6PR3N4nqMmB1+8Ox9OtQqMw59cFy7LXNaYBkdSOO8arm/jFkQw5gNBVlyonapmO5j2gV10HtFITlkuc0ap2t7mxOcb7DyyyS2wreExVwd23w2MEt5Ap8wORuYwevI1ZhjM2SVmtfUGFpkXI48vD9knu2yi3JCktOzYTtKofKVYgGCW/M0rBMuhdr3GW0ycrknPUKrqpsBrJYOjCT2BkiJPlByfWeXebhEgKzfqGIWIy+/EBeuMt654n8MBQHYCS3LkJgGYwI5Ce9TJx5q7W9i0AXzI69E20aLcE2b0sF2hWXY8A4iTDDCnngj2p2hspX7W+lYiBPh5+e5BvrCwawMMSGJ8p8o3zPaPLj0PoKZoDnRuRrViGiqZhDWr3i2mtyRsRiNsCTGQJwMuscyDy5YeC4QFxvHZ1O00JEzz6nSM7KdFrRIQlyykMp2iTkDMiQpk9OQz1Jdri4ALnrUrF5Fr2HjxzEee7RxqPDXxFeypI3wQW2E21aMEwZGJEGD61MNLm40XEio2m150BjjulDWr4JklRAO3aDINsblZTnBECP7mbNJa2Xc1CswF4FMGLDz38es03+HNLubeig4J3Nyi4ASB28xOKjtBaGZ9StTc41MJz18ARrnoujt22QElkURhQNonux5n2FcBIdkPHP8LqwEDvO8BYfcoVpcfbuA9FAtW/+Rya1mnQepV4JFwSONh5ITiFprYDeJasA48qsT/yifrTMg2AnmUxDjdxMcBH5SHUtZyxF3UH7znYn9zzq4a82JjksKjWGGgDnn5C6QnTXfnt2wqz8/TOfnf+lNja2y6G0XVR3yT6DyWbaViRB39yCYGYjeYBxRBLslRzqVEd4gIx+KPZS6lq82mVolN+6TtjdJEz0MVPsW3NTNTO2Oc4CkJC5jXaoORvuXL56DMfhk/pVQxjRn5Lp7Ss4TAaN56hY3C6/csj/wDb8BLfjVCcOQA5qIwP3vPp9kBdvW+u643cmB+HPn61Bz2fqJK6GsqaQ0eZ+yAc57VzkXuugZKpNTkaor01sZFllIFegGgG6VPeB8QFtCJ2knJz5h90weVIXMD++NFy7QyoTLSg7zBmlRAwP81XZyHtkZSqfSIK30VkM6oW2gkAtBIUHmSBkgelWccIOqUnXRMNdpktXClq4Lyjlc2Mu7GfK2edKx5IuIKEA3BWlpicFifugnA9BWAF0D3TIyUk9zFZMTuRWmuScCT+v0oFJEaphbJJ9fQf2pCjZo4Im/owLfiG5bBPK3MscxMD5fY0od3ohEZL2i0j3I8NGY9YGB9en1oOcG5lYE3nJPtL8PXwpYXRZaDtZckH3+X8656lQEYQpmvTFzcennl6oD4g/aNSpZLrLdsr+906z4dxV53rKgebHzLmDUwcGfn16LEB4BYLeX2VVvNcs2Sp3qUUHPysohjjkRBM/wB67aLsVIHwK8TAGbTUYe6Zkcjfy3ogpbSwBBCmSG5xMrB9MDPMEyKaY+yIxvrTIkeouUJZJJ2klRJZX3YkZM53MCSoz1ArNbBtkmqvkYiO9kRvG77HmlnEkuQoEgTtidsMWOMCCSGUTB5H6g4sMBXp4C7Ed0+EKNewS4tpQUAyCIkkIpDZIzPUEQOQ5yhYQYVaL8TS/OfS5tyTi21u4kXCEcfNcSAwJBB3BCOajlJIBj1qgZi6hcPaPpGWfSdDe3CVkvw/dLyjoTBzuhjt8pBV/MD5VnrSta0GfifuqP2sYQCPUD7eXoofQXbKoNniEFiYZTEgD5ZWGxM8u4OKYAtjCVP+YZXL8Vso6E8Aixwf5CBa8RZOGTcZYlcgmTBGeuJpmAZj2Uau1HGQ64NrHr2WmrsXBcP7vyAOm9Tgk8yOkGSCT09eWbLvHRBtWlTYATLhu4dR571iuljIYlEJYuRiQMCFI9BIPU86DozccvXeqtfILQLuyG7dOl51Xb8HCeBbNpw6lQA4PMjmMxBBnBM+leZVeXvK7BR7EXzOZ6i3CfBaXWYfLIM/dB/IkfjFTF1XDhGY5X9hCwv62MSC34n8EBI/GmAlAtIubczH3PqEt1Nm48l22A8wF2zy5tcE9ByU8qo1wB7rZPG/si5rWt/rVIG4W/KxbRKCCtsu33jAH/5Luf8AioNOS531O8PwPlalWpsH9Jtt5t+T5JFxLREXCbhQEkwGuM8D0UgsfYKOXOr03U2iwnryWe3aKxMuhu/IeGviUp4hrQAyeUENIuywJSI2+HkxPeKuC83y4KbKNEGAC/iOoXM6u7amdrXD3byj8Bn86VwaTLrr0GMqxAho4XP2QF7XtkLCL2UR+MZNAuP6bBVbs7B9XePHqEvdq53kTZdAWZNTJMcEVU0hBjgsq0kRmsvTQxkLLZRXrtEWKmd612xis+m0iHBCZutrQ6fn2qjAAIhTdYyFtaX1j2rFgcCCUC46BF2R3JJ5yaRlMNEShJ0RvjM+0EL5RtXaoBIknzQMnPM1g0yZWs0Kl/15/r/mnhKHRlkjuE6S5cEojEDm/JFHqxwPqam97W5poJ5LttT8IXbNoXr7qokCEIZjPIySF+oJrkbtTajsLM0rwKbZfl5rHR8PA81vTg9nvNj3821SP+0NVZ/ud4BctbaDFhhH9zreQ1XQ27IUbmuXLsfKAFtWge4U4P1muckm0BvqVJtRjrsa6od5sPW3or6O3cZw2y2B3LNdcj0P2fpQdgAsT7BE1KjjDvL9pPoFfivCvFi4jlLqHcjriCO56j0ZqjOh665FNTqlt/P8m/q4LkOK2XUXLlpfDvDz39OACjx/9RYUgg/zAcqemTTJLTn1ddFalT2gNLhMdZq4vtct238ptlAHUg48NYJUKMMSuOQznFd1Jx7ME3Oq8Oqxg2l7PpNsJ55IfS20bctsj5tzq8eYkhfu84FsfNjPWBViBikLFz2NBqCbWMyPDdqTko1dxQVS4VhTzQkkbdo2iPKAI6EfNzxSOeG3CpRpuLTAz5a+/wA71f8AY97yxcM24FJ2ttO0hYiQsbQQZypiMVgA4zmMxwRdVNGmWi0WPG6WWbjsSSGV1Z9rLCwHz8ygblmPUd81mMJJLhdXe5jGhrHW9euhayMs8PeSTkrjdIJXBkCSNomO4zinDWk4pXJV2nA3CWnyzyjmiLWnbfuLhQuR5lbocBclpmOXSadwGqkKxjuC/G3v1ktfKrglvs4UI0nng7lEcyPSlk5wkLC5mE2vvy6/dY8Z1v7NY2IxJcg7SAY25yDzH9/SobTUNsP1Kv8ADqHbVXVHgYY8CZt1ouK1vFLl0ybnrEQB3iIFcTiXHEXXX0FOmykMLWwOs00+Evie5pHjLW3I3WyYD5+ZT0eCII+taAbO8FniRI8V9Vs37epRblq67WmGAnlkjmrbRIYdRj3NICW6D397LkfSa3OY3ZDyaJPV1CaW4GIVltoDgKC1wj+ZiTB+tPjbFxJ9FzFhJhthrAvHqR4kJfr+LpZBJNvxJ+UMWIHdmEmfaPpVBTc4cPIeARptph0taTyufFxsOQKQ8a4zeCB96+aIRXAaCJBIQl49268qZjKcxc+3Xgu1tKoBNmjzPmVyOr19xic7Z5hcT7xk/WunkITsoMF3S7ib/hLLl0DlM0JC6w0m2iCvXO31oTqE4GhQbGpwQJCa2SyapkTcIqhNTL91kYUGomSsooGwzWUUI3LI61b7/lXthoGaiXHRaFcZrcCl1kKqmtJKJgIuynQ86eIsVJx1Cf8AAuC+NJuM1m0ASbxtu6yMbQF5sf6VGrVwWAk7kARnNlrb0llRFy/J6LaViT6MX2hT+MVg9zh3R5pi0AyVfTX7cnwtPyjzuBcMz1LRbQ8yPL0rCm52bvK35Uq1cUwIi+/7apk2ouMAbzD0BO4nGAoMKP8AwFHsmgGAvOdtDqjoaSeAsPST4FOtL4Sm1du3PDYTsD4dRtgAbvNEctqkVxPc2cLQL+M+X3VadGs4XxewHKZ9lrrPieysm2rXG+8cA/8Ak8k/QCnbReRew63fcpmbIxrpNz5nzM+gCL0L6m9LM9u0B0CC5OWUjxHO0ny9G5EGpOwNsJPp6D7K9RjKYlzfO/qfunduyVIJN5/YLtz12lQPXrUSZ3fKlI/ttyJHsB1mirS9QMjrzI+smP8AkKQjrr7FK6qXDO3p7/8Aockp+JeHLcCsDtuAyrjBB95E9ubVRk9dfZI2t2ZvkfX2n/kuH1PjWQ5RFkybtplJVo/6tuYIHeIIpw9zTLDfVdVXZ6dYA1ByORHmPhV4ZxvTuChXazrG8Mx2loBkR1iuj+Z7wJjjAuuGrsFQMhriYNpgCAmr6R7aN41sS25hcHJ59BggcwBHryq7cLsjK5H1HQCLX6vktLehdLSlf3JPzXGBkJn5Rz3EkSY5YpMIFmnwWNftah7QSMut/XFZtZIICq5BAJLBs55BZgSOpqwN1Hu/VPgIHrmVlrLoW4Z3tcEGG8oxkKTJYxERzgR2oAWhWDnOGLKbakhF297oJtLHNcOS0hV294AXA6R+JgTn1f7rkdVa0huLeZ4RHwtmsuiPcuQu1ZCrEk7TG4xIx6zSOqgfTdDshULWkWJF9b8/svnPGdY9+4WZo6L6QOUVwuaXmSV9NRYygwMYLBBaKy9w7FBY88LJjvFKzEe6eaq+B3hyTTS8Bkxde3bGJWDcuDMfKhgT/MwFEt4Dl7oYtZO6dOEyut4dpdRpbVwaKyzO4ydS0b2UyQthIC3IkiSZyPSkqYgOXzry5JGvpPdhcc7eI/SePPMZKdfxO8423WKkdPlE9io5V0tgZBcwosmbuHoOWiQahwJBGfy/CnHFdYBOWSXXrp6GPypgqYRqgLjH/wB8UwaVSQEJeuT71jfLNO23JCXH+lTcYO5MAsWNI7v5Zo5KttZIE8yB+NTyvPXssTZd3xTW6ZtL+zLpbC3BkskqVZVY+IBt3EwIILdYyK2BwGJczdpDrR9s/lfPya5i4rqUUh3hZRQssm+nt9z/AF/SvfAixXK52oCvct5gwJIEmYHqY6fQ0HHCDIWacVwU0+Ivho6Pw92o094uJK2X3FOokcypHJoH6TGjXbVJAsndYLDRasKNot2w2QXYFifmHJpAw0YHQHmJqxZJuVMugSBKMv3Lt8AveOCfMz9yCw25J+acDvzpH0gRDbcQomoGmCJ1iOgMlNm7bt4k3CAV5BV5RJJBYn6A1VrcLQ3cpObVqf4jnJ9LD1VdXxe6xwQh/lweZMbjkZJ5HqaPAIM2Omy7r8/tkiuCJeRvEDtbYyu4naSDEgT5jMjkDzqb2h4vdUO0MYcLPIX9reZC6izwBLaC/eW6hZiB+6bdcMBpDXI9exMHFcoc3ERTgnmg51Zwl9hxv7WHiSrWWLMRY01tTzL32DMASBJDchJHSM05Dol7vJSmjkJd7fDflMNPxPChr+87QQti2qBViYNwgbQJ6cqiacmw8z8KhHZjGYbyEnl+Lpro7GTsFtCPmg+Nc/8AJ/lH+5qRI3/A+6lWxNHeaTOU970HdHMloRBe4cIx3E5uM9swOyWw0qPoT700NAk+QB9TF1ysLnOEDxLgXHgIxR4Ia3ozbvPc8V3cqEMnkJBMLBYTGcClc4OaJFuuQ9SnBLXkNz13+JhzvNreaE4noRdG4GHWdrjJU/8AcScehce1AWt114FUpVXNOI3Hn6yfV45LieJcMIYsq7HUS6KMHPz2+6nqByp5BELuz7wy66tZdvodXvt24MRbIj1gmmjvLx6zAGGbj91tqHfdbOeRnP8AM+I9q2ET1uSB8Uz4eUoVHYsx3MBuJ59yaeO7CR5708D7I3WPtIPY8znp0/3pSM1RrAOwmLnVTa1RDNJJjdAJPLMD6mgQFRjC7Ld8pDxPXo1u5bL+ZwPKPMQNu0mF/mMUcTZhdLNlcA1zrBpmeugkek+G1JP7tsZLXTyETuFtPmXrzOIORJAIECLzl9uBXSNpaHOacxmIuBv4jfGQXQ2+ACIuvK48o8lsTjITOxujjIODmCVuer+HEajyU3bSRlHuL7zkWO/S8ZHPUInRaezaurZMC4FPhuREg4Nq6Yhz9ciDjABwyJ8bf9m/IXO6q6c+EO0/wfw/tdpxBu5PnGwsbZAKTzCkiE3jqobaVfmIjtKGRdvPnvj5HQpT7O4eLHuknNp0Dv8Ay71yK5vi2jN1mt3ALerUZBICX16MG5SRyPXr6UbEYmfT7fj2XU1zqbuzq+B38D/lu381xmrMMVaQQYIgiCMQZyPwroELoExICV6q50iKYiLEKjL3BlBXHn37/wB6w71k/wBPJDqhYhVBLHAVQWJPYAczS2GZhPPBacV4ZfsbPHs3LW8bl3qVLAGOR6+nPI71Jzw/JEWS5jUnOJPFEKs0jmkm6yNu8Tcrt3GIiPpGe9TL3QBKkKLQ7FCAoTOSqq1O+iyihYrJ5pbfcj3z+nOvoGiQuR7t11pcf8RyJ/QjtQf3mkINEIe5qi0jbAOeZPUnqeWTXPTfVc/vCAAnbTDRmtLRrrSHgi7ZEZmhZC82WqST0B/M/XvTC6V0NW9hbkSrqmSdxI3mCDzAL4Kj8T0JpLkqNTsgYIJ4afA1W+kS2SYNy4205A2nA6KCSSPccqSpdpnciTVaJ7rRz+ch5FdZreL6i8ltbmqfbjBIUGF+2Vgs2Ptmuens1NkOYL+K5XbYXkteMQ3ADzO/mLIFbNomBvvP9xQYMc8Dr7E96uTF3FFv8y6zGho8z14BMreiuBfP4WnTs5G4+mwAyfdR71LtQfoE9b1uwptdNR5LuEyPKSPZMdJdFwbFa5f2D7R8G0qjqQuY+ue1RPdvYTuuVVzNS2w1eZjwn5TbT6NgSu5bfU27ChP+RILt77R71A1AbgeJM/j1TOaYh0n/AIjyAxHxCA4sDISyduZIC+I0DmFUyu6TJZzOBEVpm/XnaOQUWgNcWOA4A3jjgbJPEkg8kKnEVDMbl1VCEbQG8R45TcIBIYnkisvbzc6waXZfj1+xVKncABbc2BJ7xP8AiG5eBbHBe1FkajzKly2wyruu1iR/JPiEHuQwrGwtf2HibeUIUiabof3Z0zJ8G38y5C6TU5uJhXCvvtzzJWAydQP5TBFUY/FE9eKG0ULS38xyTXSao3Gt7QTgEQCZB8TnT2bMnqy8+rSc6mcAk7lS0yWSRfuoph/Is3bpzz8O3MYk+YiKR1UGzRPoPMrpbsTzLnGLczlBsETqdYz/AMLTbQP+pqGiN07SbVs/KZIBJI7jlMwXb/L1z1G6Aq9ns7LG8Rc5CciY/ScsVwDnrAV7hruZv3C3TYItrP3CF5N1V+TDn12sB1n48RvGYRO0R3WiNIyv/aTkHascLOy5jaTwWZrdtWS5bY42gXMSviquQxIwyHD5Bzzz6YsT+3A8Nx0QpbS8OnMHMb98DR4/UzXNqo3Ftl027wFmAHs3lYlGUCWIbmE3BjBkr653Mx9iHeI38efv7TrbIHlj6Rt+lw/SdBxYcozabZWDJixUgHw2UbjABC9SwXk9oj5kGCDIxlS9pzBzyO/gdx3HwN0lCqA/C9vebMt3Tm5o1ac3NvGY44taVwpbyscLdRt9sGcWy4y1tuYDgETGT8xY57SYz1G/iOO+OapUZRLdCzKf7OB1w7jm3llpa1Mm2t+bbElUuA7lYEQybxKsCDjO4R/yzwCJp84+R1f21BrqDi2sJbEYuG53AeQ5GwnE/wBqtractvuaZiysuWa207mCmdwACyvOGYiRmpzTd3ogOsefwuxodTmi3MXbOogWB1gzxAjRc5xS+Nc297gN64YtXYVUuGBFhwICv91jz5ExBWzWNpgYfp8/H7hUoVnvlrxDxpw38v2K47VkqSrKQykqQwIZSMEEdDPQ1bEIsukMQV24TSueTmna0DJOPg7VXLOoF225tugnAJ3KSNylPtrtBkexERIlUpF0NdZR2itgZib+OROkp58afFF3W2CpCC2oFzato4fewxceTyzK7eZGc1PsDSglJT2gufFhe282+6+ek0CcRuYXZkqmomSYWUUIk3KygmkLtwWVaRFerQgn2mM5Iic9ueYzmK9+lJYJ3LjdY2uoukdZpraphOiHTJ6Ci2DwRda+aJsISepP+85o3Km4taEaiCIxP6+nvQSyQZ0Rmk0Jdd2EX7zSA3OIJxzEc+tCdylU2htN0ZncMxl46yiLn7OvzbrzdIkKcn1EGNv3hg85rc1EfzL/AKQGDjn1nuRunvXSvlRLKHq0Dd+Ign1Aml5KJpUQ7vuL3bhfrxKoujs795L3X7yQB7FpIx/LUTTGLEevhdlM1A2GNDRx+w+67X4e41pUsMLuluC6N6gWgZuKobzKdy7HUXSCTmDjsvDVFZ1Tu5fsiHUQMNRxJ9DM7reeW9I7GosjzG0zuTzvPAA6TtgMw69OwiuvvPAMxy/KDMbAQwADTUxyHyUw3XriATttmPKiratH2d43Hn8ob60ksYePmevJEUqjzJExliy/+QmFvTsq+d9ijt5ByiWe4NxMfaFvPeo4gT3Gz6+gt6qlRjRas/wFvQXPqs9XwxTBE7W2lswLgGQr3HJa4mQdq7Qe1DvE945aZ+gsFyVa7WDBSZANpJweWpPK6yuqLQCIy2j0VNlsx73CHIn0602Jp48/sLKDKNX6nTfcI83OIcfFDNrtPp0YXLxJJ3MjXDcM/wDapA5DuR6VjJMnrz+yZgJEU8uHzhgebzyXMcc+LEcDwLZDKZRyY2nrCJAI5c81J7xEi56339l3bNQqMNyAOtBDR5E8Uz4RqX1Vob7rgqP3lhSEWJ/iKq5ZO8zB5yDVqBGTxfTo9Fc38QFRjcdE2GfDjy36jPiOv4RatKv7tVDCGYJG7sLi9d2MifNHfmKjMJjTj7HhuOi46W0OriTMzpnIH1M0xAfU3Jw0zCtq9aEZZK7WKoIGAbh2goPtWm5Mh+U8uoEyYPD1tv8A8hodV2U6TarQ0QHXIIuCDnA/tP6m/pPgSt0/FLdxZUwCVt7WnBcb1tt1ZGAlW5qRzkS1MWvj+Rx3jVT7IwLC/djMDMYHb2yDhObTwslXE7tpxbvpdZUaB4oG5D2t3gCpVxGLgjA/lAUyQcIjloeR+NEQ3E0ktMg52xtIykfqjQ3xDQ5k7X3FCAanaVPmFyAwIYi2bqyMNLqrYAYNOCDQA7wjkJ/6n4KwOJriNYLg2YO57OMi7d/gSFqrAt7FtXDbvW0m2xbyXUkKPDZuZEINpyMc807HAEt35g+x+Cg9jnNFYwQNRYwMnDKDchzfLcb8A4vbaVuC0hudQoW3cnmtxRgT1PPkRyguWW7s201HFv2TVWvY7FPCSPR0ZtO+Jab70Hf1iJcZQpbf89liZeGMANy8Uc1cE7hH2iQdBdfJw1+fuFZv9JvdINM8Zw8J1bx/TyyYafjZ8PwzdUoZ/Z9Q4ICOvmKXgIKXAAZ7iWE+ZSuHEcQF9RvG8Iuoim0NM4LQRmw6Rw3ZxkZabJdTxO5pLo1VlH07EvaugBTb8TYjhgIKlXDsVjB2EjrAOCMLrtzG/X2yVi2rhm2MWkDT40MJZxO8us81xwbjYt6hoXc3/o6mMKZ+W4MZAMDCHCKd2ju7uvUKlCq53cfZ4z3Hl1I45nkdVbZHZHUoynaykQQR0NMHg6wOC6Y8VSxfKMGHMEGfYzUagII4LOaHtIWmu17XBDtugADsMz7fhSOJMYtFOlSDPpET11KANIXWhWVZpZmxWURSlsZrSomhM5rKCaQuJWXq3gsnGmk/7/WvoGglczyAtLg9RP8AvWjCAchx7VkyLtGcdenr/mmzUiMN9Eba1ELACjGSRJM7h1kDDRiPlB5iaWEhZLpJP2y+R6kZLQ3y53OSx5mT82ZOehyfee/PLNphghgge346yy2OvYfwwtvpKjzdvmOZ9o+lBL/LNd9ZLueXkr22LeYnPUsefrJoOMp2AU+6MuGiahHtAbt6FsiUKyIKyGImMmQBUsQOSZ1PGbjz5zl4b17iNy/akWbhvFyWOxSqJiP4zmDLA9BzHtXLjfJEHgpvo0mEXjK37Xy/KYaG21tF37EdVBYqJaVCktL5XKgyikCTTtpnD3uvJT/nh9NJs8+vchdePhO6bf7R4ltmgXAxZrkrz3eJBDYgjaAex5VzDa6QOECyoaO1VPrfHAdfdBabi1i3YZ20txtQC37wtIEMQrhnO5FMSUAnPPkSHis4/wCO5ak6iG4WTO8a+ISrinF7jq20nrO0lPTJUl2H/kParCmwZ3660VBRqaAN4/U7zPzK5i3xMW7b7rXnMqDvKAAjB2r52Izkk9PWTLh9JACgaFInvguPG/4C52Y83Pv/AJ9Kibd7Ndck93JV3RMcjOB0/rQDoJjJEtBAnNHcKvvbdXQ7XUyDMR6Geh/OsGyIKYuErt9NqBqIv2WK3UUi7aUnCmfNb5eXcQ0DkcdiKNdjMON/f8+/NeZWpfy7SWN7sh3+0iL/AO05H+3dhkA7itm9qNPNt0JLK64EG4oIZZOEdstOASOmdquxN8PbQ8Yy3hPRfTL72Do8H3kcMQgjR3Em6fh3xEjbm1FuL6fxD8rHYSN6qRi8pLSuJkxBJpQ4xGe7luPDduVqmyNLiWmAbn/cMnDcd+YOoWWs1luywuWgG0983Ld23tPhsVK+ZB9nd5jtxlCRGNrAD6DlmN469VOHvl4/1G2J/S6wMHgQZ1LTlIznW659Na/cnx9Fc8vnALJuBHhtIwexMglRiVgM6JDXi+8ahLRYXy+mcJ1bmAePPeInNZ6K6AgBLXLJ2mB86tbUAXrU/LdUAbk5EZyDi7qZ+ppv7/j2SUaoBNGsIknwxTbkZOE65GDmNxXRFRuXayMCwK4V1HO5bHSPtJzQ91OHaQ4SPEbutFcONJwpvM/2u+HceOvPNPb1q/w7klJww+ZD95fTuvX3g04I1T1KLh/UpWdqNDwPHcfOyseJPauEXQtxHVRcX7N5Jw4YZ3dnGVI6QRU3tk3txVdmLMH9PKcjod3Do5FMtJxBLYVHYXNLcBS275NsSGaxfRclASDK/KSHSDuSoOYSZGfV+uR3roa7eieF8KtaS9cu3rSanSgDdbZtzW2ZS6BgvkfEbWI2uGkbTICkvqDC0wVGq9rCHEcOusskH8V6/T6y7BtJpSQVsXQxKeRioS55Vi20CCB5J6qcKGupgjPrTr1T0aoqiR1zXFazTvadrdxSrqYKnmD/AFBEGRgggitjkKsaoeljfZaVU1MoqDQJORQUULwsopbLKKErJnwrhwuqWIJho+aOgPY96LW4rqb6mAxC9YYn3r32y5I6Gq5aetZDJQDPv+v+aOa0QtkudPyGKMkpMIRSCRyg/r7UYkJJg3P4TThHAtTqf4Fm4+Y3RCD/AO4xCz6VF9VjB3iqAElV4lw29p7rWrqlbi5juOjKRzHqOx7Gix4eMTVnACxRGi011WDz4bDzAsSGxkMF+Y+4FYtxBQO1Um2bfl98vVHX9SrEFme6/LJgYECOZIxyxSBrWiywdXfJMNG83PwB6rZrjgASLIA5TBz2ABuQfXFbkotbSLiTNQ8rfDVg1y2AcM+DMnaPwEk+8j2pHZXXWG13CBDR5n4Cy1Ot050qo73GQKNtpnbw1IzItzAJJJ7T161zEUwzHH3Umdriw315ee7dqFldtXmkK/7vcX5kRuacAH6fhRcHLpGzNDsk2a+ekL6D9J5n60V1CmNb80r4noAULL9fT/H+9pBup1GJG1kgf0oFtlzGZghUVIG4Dr7/AJGkwloxALFwJwuK2skhgRnn/wC1YAzKJgiCj9LqWsuty221hkdx6HuP1FLUhPSk5rqrXGVZGvWBER+0WdsgCRLqAZ2E/aGVMdgaYVAbE30PWvoVwO2IsdLQC0iC2YtuyuNQP0nIwYQfxBpU1LAoClxh+6csu3UBSQLbsIAu7QpVjEztMQIz2Fl9DnGX7JtkrtqSyZc06/VEDPjpOsZnMqODcS8LdZvpusMdro0gqQckdQwPbII71QU8Tb5aHd9wmqNIfjp/VqP7h8EaHwNlbherOldkf95acQ6YKujdVJ5+8Dl0IxXsxGF37LQawFWjZwtf/q4dEZjjTUaoWbn7sHwWIZcySB1D8w6mfUcjPWjSW2PXFZ1Nm0tJycLX04Eag+ouLrpPhQ6R3K6h2Fh4cMpCIl1c+IY81kxgkELnPlYRzbU5zCHUs+vTnkhsziWOo1+UHjpOvA5nI3CWf/6HwvRrcD8PJIKzctBW2AD7dp25+oWR1wJobM+o4HGF0mtSbhaHcAc+Fz6XNzxXMaK3day7NauPpkPmuhCVss0ZDcgTKyPY9qsXtHdJzyWqUTPaU7O13OG4/B0ySYiX2gzmAQOYmJCmOfYx9KkSugG0my7LW8TtaJLa6TUHVqV2uLtpk2Bjua2IOUbPkk7WBYGTIgWOJlwhAltQRmue41plcHUWWZ7LGGDGblhjHkud1yAr8m5YOKYOAkOvPVlmswgALbgt63qWt2NYbnhrAW8kG5bTlsMg7rckQIO3zQMmlIdkNfVM5wFyo+NOHaS1cH7Fcd0iGDBoVgBlbjAbgRnl9YIAAJiCEAQclzdTIg3TL1DEMllFJKy9FaN6y9FAwFkdoeJXLa7VcqJmB6xTsrOaIBUKuzU6hlzQVmtw17geSnwhMOHaF9RcW1bC72wNzBQTE8z+gk01R4Ak/ukaItKZcX+G7uku2lu7GLwRBJQkESjTDdugkHB7TxgsJbms4kX0XSfEvEbL6YWrOjtWivm3IQCjKFLFAqjcGkjJnHLFSpsrMcHk52XO3aKdQ4YXF2yT3J5/5rruVQwBBXY/B3Gr+mRzaddrxKOpZA0wX2giGiMciI9K4amzGtUMcFB+09kcMb8/Tw0WHxDxnU3HL3NQXglVhVTaAZAG0CJie9PRoik4gIsc3aGjtAJjL38EALloSQGuH18q+8CSREYkRXQb3KwFaws0eZ+3oZ5rVdc4HlIQdlhT/wD031mhkiNnpOPfl3O4+wVfEnI+o/r7UhvddTBh7vktBezIx7f5pCqBtoN0G3B7TEtmPuA4X26x+nKuc7OyfhMBBgptbIgZ+mcVQqgmYhEq8DcsY5zBM+xxH0pY1Sm5wuVEczj/AH6Uqq4CLrDWaEHIHuOq/wCK0qGEEx0Usv6WDj8x+I9q3JRdRJzVDZIyJg4P9j6ViNymGXh2a8bDbZgx3pOztKrInDN1rotQ9pluWyVZTg/qD3BGCKYMBEFKWmU9t3rb23ZEiyc37AJLWCTi9aPPw5/48jiDT03x3HZaFcW1bAXkVqRioPI8Ck/xBYueIHdzdDKu27HzqoCiSObAATOafswywV9k2ttdpkYXCxbqENp9Wu3w7pGzoRlrZPMiOhxI+ozVBlBQq0nYu0pfVroHfkaHwNlm1/wibVxd1ts85ieVy2eU/keVYOAsRZAs7YCrTMOHRa7qQvaa8bBILHYwLJcTqIzHrBAKHlP4yLgx4nJLU/8A0NkCCLEHS+vw4Z+xeo4ittgWD3bNwj96W/eqQFG62Y/d3VgYMhhIyCaFR7i4OHgRl1vS7GxrgaTxB1bG858R5cbofiSMLTeC25HlyEJW3dAwXCD7a/atnK5IlSDWMOEtAnXeOXBVaH0XhrycOQPsHfB11vmm0nFylm5ZKIyuQ4JB3I4gb1YZmBETH5zBzpysu6BqrcZ0t+2E8UeVxvUqQUackgrgtnPv60rXOOd0gptbkl9jUOm7axXcpRo6qwgg/Qn8aWAM08q2h1WwnEhhtZTyIP6e9KKhabZJKlMPHFW1d/cNqqAoJaFk8hBYkknkO/Sg97nFamzCg4pcs069FLkiopZWheihCymKx3IKIpVkw0PDr1wM1q07BZJZRygTz6mOgzX0DXEXFkhaDmp4ZfCuC0++ZUyCG/Gp1XCAXCRN1OoDh7pgrfX6tW5Hc5IJbviOc5pA6nUcWsEW5oUw8fUqXuIXHgE46+uB+PLrWayoXCdPVBtFrcl7xZ/3H0rsJlYNha2tY9vcVODAj29P61x1mua4vFwUH02vgFeW87szt19SYz65ijRY7GXkQEzWhjQ1bi7meXtXSSmDbQbrdDiR9aELTBgre24EGc9h/sUqa5tCa2dB+4OpF2yIbaLRY+IfUKRBGZ/HtUDU7+GD8Jpb9JN0HbumZFEq0AiCiA2JH1Hb/FKUWnQq4uwRE8sz+Y9qQpgCRBVhqD0Me2P050E2AarS2TEjlynpn3oQg4tmCqkCJOfb+5opSSTCzDDdIEenP6VpSmmCIKvftrzBJHrzFMUjRoQt+B2dKbo/azcFqDm3BIYcgwgmDnI/zSP7SO4JKV72tMFL9TrVsXzc0pfYrHYbgG7aejKDBBEjPMdByp2glvfHNYHFkUU+rR7LvbTdaibunBzYb/1bRz+6n/jMHBks2pHdf4HrX3XJX2LE8VaRwvGu8bj17LmNdpykMDuRvlflPoR0YdRTFpHJUpVw+WkQ4ZjrTcUE1z1mhiA1lVgngvJrWCMn2WgwehHUdjEj2JpMVoSuotc8P1HUH3XtJrim4Eb0bDoThgOWejDmD0oMdh0shWoB8EGHDI7vwdQpu6prcpauk2yVuCMEMOU/dYdYOcc6DoacQKZhNRmGo3gRofwV7U7boNxQquBLpgBh99Onuv1EzADi10uaPBSp4qRDHSRoc44H4PgYiSC9xiACSQMAEmBJJwOmSa53ei6lSlE+CC9FKbcQijuFcTewWNtmQsu0lTBKnmp9DWD4zCVwJyKBNTTL0UZhZRSysvRQWXooLKa0rL//2Q==", caption="AI-Powered Streamlit App")
import requests
import json
import base64
from langchain_community.llms import OpenAI
from openai import OpenAI as OpenAIClient

# Sidebar - OpenAI API Key Input
openai_api_key = st.sidebar.text_input('OpenAI API Key', type='password')

# Dropdown Menu for Navigation
selected_tab = st.selectbox(
    "Select a Feature:",
    [
        "💬 Chat", "🖼️ Vision", "🎨 Image Generation",
        "🔊 Audio Generation", "🎙 Speech to Text",
        "🛑 Moderation", "🧠 Reasoning", "🛠 Functions"
    ]
)

if selected_tab == "💬 Chat":
    st.title('🦜🔗 Quickstart App')

    def generate_response(input_text):
        llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
        st.info(llm(input_text))

    with st.form('my_form'):
        text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
        submitted = st.form_submit_button('Submit')

        if not openai_api_key.startswith('sk-'):
            st.warning('Please enter your OpenAI API key!', icon='⚠')
        if submitted and openai_api_key.startswith('sk-'):
            generate_response(text)

elif selected_tab == "🖼️ Vision":
    st.title("🖼️ Vision AI")

    image_url = st.text_input("Enter an Image URL:",
        "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg")

    if st.button("Analyze Image"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "user", "content": [
                            {"type": "text", "text": "What's in this image?"},
                            {"type": "image_url", "image_url": {"url": image_url}}
                        ]}
                    ],
                    max_tokens=300,
                )

                if response and hasattr(response, "choices"):
                    st.image(image_url, caption="Analyzed Image", use_column_width=True)
                    st.success(response.choices[0].message.content)
                else:
                    st.error("Failed to generate response. Please check your API key or image URL.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

elif selected_tab == "🎨 Image Generation":
    st.title("🎨 AI Image Generation")

    prompt = st.text_area("Enter a prompt for the image:", "a white siamese cat")
    size = st.selectbox("Select Image Size:", ["1024x1024", "512x512", "256x256"])

    if st.button("Generate Image"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.images.generate(
                    model="dall-e-3",
                    prompt=prompt,
                    size=size,
                    quality="standard",
                    n=1,
                )

                if response and hasattr(response, "data"):
                    image_url = response.data[0].url
                    st.image(image_url, caption="Generated Image", use_column_width=True)
                    st.success("✅ Image generated successfully!")
                else:
                    st.error("⚠ Failed to generate image. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")

elif selected_tab == "🛠 Functions":
    st.title("🛠 AI Functions (Tool Calling)")

    st.markdown("""
    ### How Function Calling Works
    OpenAI's GPT-4o model can **call functions** to retrieve real-world data.  
    This example fetches the **temperature in both Celsius and Fahrenheit** along with a **weather description** using a weather API.
    """)

    # Function to get weather data from Open-Meteo API
    def get_weather(latitude, longitude):
        try:
            response = requests.get(
                f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,weathercode&hourly=temperature_2m"
            )
            data = response.json()
            temp_c = data['current']['temperature_2m']
            temp_f = (temp_c * 9/5) + 32  # Convert Celsius to Fahrenheit
            weather_code = data['current']['weathercode']

            # Mapping weather codes to descriptions
            weather_descriptions = {
                0: "Clear sky ☀️",
                1: "Mainly clear 🌤",
                2: "Partly cloudy ⛅",
                3: "Overcast ☁️",
                45: "Fog 🌫",
                48: "Rime fog 🌫❄",
                51: "Light drizzle 🌦",
                53: "Moderate drizzle 🌦",
                55: "Heavy drizzle 🌧",
                61: "Light rain 🌦",
                63: "Moderate rain 🌧",
                65: "Heavy rain 🌧🌧",
                71: "Light snow 🌨",
                73: "Moderate snow 🌨🌨",
                75: "Heavy snow ❄️❄️❄️",
                95: "Thunderstorms ⛈",
                96: "Thunderstorms with light hail ⛈",
                99: "Thunderstorms with heavy hail 🌩",
            }

            weather_description = weather_descriptions.get(weather_code, "Unknown weather condition 🤷")
            return temp_c, temp_f, weather_description

        except Exception as e:
            return None, None, f"Error retrieving weather data: {str(e)}"

    # Expanded list of locations including Miami
    locations = {
        "Miami, USA": (25.7617, -80.1918),
        "New York, USA": (40.7128, -74.0060),
        "Los Angeles, USA": (34.0522, -118.2437),
        "Chicago, USA": (41.8781, -87.6298),
        "Houston, USA": (29.7604, -95.3698),
        "Toronto, Canada": (43.6532, -79.3832),
        "Vancouver, Canada": (49.2827, -123.1207),
        "Buenos Aires, Argentina": (-34.6037, -58.3816),
        "São Paulo, Brazil": (-23.5505, -46.6333),
        "Mexico City, Mexico": (19.4326, -99.1332),
        "Lima, Peru": (-12.0464, -77.0428),
        "Bogotá, Colombia": (4.7110, -74.0721),
        "Santiago, Chile": (-33.4489, -70.6693)
    }

    # User selection method (dropdown or manual entry)
    input_method = st.radio("Choose input method:", ["Select a City", "Enter Latitude/Longitude"])

    if input_method == "Select a City":
        location_name = st.selectbox("Select a location:", list(locations.keys()))
        latitude, longitude = locations[location_name]
    else:
        latitude = st.number_input("Enter Latitude:")
        longitude = st.number_input("Enter Longitude:")

    if st.button("Get Weather via Function Call"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                temp_c, temp_f, weather_description = get_weather(latitude, longitude)

                if temp_c is not None:
                    st.success(f"✅ Weather Retrieved for {location_name if input_method == 'Select a City' else 'your custom location'}")
                    st.write(f"🌡 **Temperature:** {temp_c:.1f}°C / {temp_f:.1f}°F")
                    st.write(f"🌦 **Conditions:** {weather_description}")
                else:
                    st.error("⚠ Failed to retrieve weather data. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")



elif selected_tab == "🧠 Reasoning":
    st.title("🧠 AI Reasoning")

    st.markdown("""
    ### How Reasoning Works
    The **O1 model** introduces **reasoning tokens**.  
    These tokens allow the model to **"think"** before providing a final response.
    """)

    reasoning_prompt = st.text_area("Enter a problem to solve:",
        "Write a bash script that takes a matrix represented as a string with format '[1,2],[3,4],[5,6]' and prints the transpose in the same format.")

    if st.button("Generate Reasoned Response"):
        if not openai_api_key.startswith('sk-'):
            st.warning("⚠ Please enter a valid OpenAI API key!", icon="⚠")
        else:
            try:
                client = OpenAIClient(api_key=openai_api_key)
                response = client.chat.completions.create(
                    model="o1",
                    messages=[{"role": "user", "content": reasoning_prompt}]
                )

                if response and hasattr(response, "choices"):
                    st.success("✅ Reasoning Completed!")
                    st.write(response.choices[0].message.content)
                else:
                    st.error("⚠ Failed to generate reasoning response. Please try again.")

            except Exception as e:
                st.error(f"Error: {str(e)}")
