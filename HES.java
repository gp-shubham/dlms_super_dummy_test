//package hes;

/**
 *
 * @author neha
 */
public class HES {
    static 
    {
        try{
            System.loadLibrary("HES_SO");
        }catch (UnsatisfiedLinkError e) {
            System.err.println("DLL failed to load.\n");}
    }
    //Native method in C...
	synchronized native int apiDLMSENGINElib(byte[] Java_InOutBuffer, byte[] Java_pAtoSBuffer, byte[] Java_ThirdArgumentBuffer, byte[] Java_FourthArgumentBuffer, int RetVal);
        
    public static void main(String[] args) {
        
        HES ObjHES = new HES();        
		
		/////////////////////Block to call C DLL /////////////////////////////
		
        byte[] Java_InOutBuffer             = {1};
        byte[] Java_pAtoSBuffer             = {1};
        byte[] Java_ThirdArgumentBuffer     = {1};
        byte[] Java_FourthArgumentBuffer    = {1};
		int RetVal = 1;  
//pls note that all buffer first byte is one and RetVal is also 1
	
		RetVal = ObjHES.apiDLMSENGINElib(Java_InOutBuffer, Java_pAtoSBuffer, Java_ThirdArgumentBuffer, Java_FourthArgumentBuffer, RetVal);  //Calling C DLL 
		if(RetVal == 0)
		   System.out.println("C DLL load Sucessfully");
	   
		//////////////////////// C DLL Block Ends here////////////////////////////////
	   
	   
	   
	   
	   //////////////////////// Block to call Java DLL ////////////////////////////////
	   
		DLMSParsing DP = new DLMSParsing();
		int JavaDllArg = 20;
		int CSVstatus = 0;
		
		CSVstatus = DP.CreateCSVorDB(JavaDllArg);	//API in java DLL
		if(CSVstatus == 1)
			System.out.println("JAVA DLL load Sucessfully");
	   
		//////////////////////// Java DLL Block Ends here////////////////////////////////	   
    }//main ends
    
}
