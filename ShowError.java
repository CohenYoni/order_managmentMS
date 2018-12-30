import javax.swing.JOptionPane;
import org.json.JSONException;
import org.json.JSONObject;

public class ShowError {
	public static void main(String[] args) throws JSONException {
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			//String test = "{ 'error' : 'some error' }";
			JSONObject json = new JSONObject(args[0]);
			JOptionPane.showMessageDialog(null,json.getString("error"),"ERROR",JOptionPane.ERROR_MESSAGE);
		}
		catch(Throwable err) {
			JOptionPane.showMessageDialog(null,err,"ERROR",JOptionPane.ERROR_MESSAGE);
		}
	}
}