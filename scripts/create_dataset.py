import create_data_identitycard as cdi
import create_data_studentcard as cds
import create_data_license as cdl

if __name__ == "__main__":
    i = 0
    while(i<1):

        cdi.create_image(i)
        cds.create_image(i)
        cdl.create_image(i)

        i+=1