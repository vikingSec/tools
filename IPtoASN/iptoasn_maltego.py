from MaltegoTransform import *
import IPtoASN
import sys


val = sys.argv[1]
print("""<MaltegoMessage>
    <MaltegoTransformResponseMessage>
        <Entities>
            <Entity Type="maltego.AS">
                <Value>"""+IPtoASN.getASN(val)+"""</Value>
                <Weight>100</Weight>
            </Entity>
        </Entities>
        <UIMessages>
        </UIMessages>
    </MaltegoTransformResponseMessage>
</MaltegoMessage>
""")
