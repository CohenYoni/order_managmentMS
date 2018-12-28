import java.awt.BorderLayout;
import java.awt.Font;
import javax.swing.JFrame;
import javax.swing.JLabel;
import org.json.JSONArray;
import org.json.JSONObject;

public class ShowAllProductsInList {
	  public static void main(String[] args) throws Exception {
		//String structureOfJson = { products: [] };
		try {
			if (args.length != 1)
			      throw new Exception("You need to pass one argument");
			
			//String test = "{ 'products' : [{ 'prodID' : 3, 'prodName' : 'table', 'price' : 50}, { 'prodID' : 2, 'prodName' : 'bag', 'price' : 100}]}";
			JSONObject json = new JSONObject(args[0]);
			JSONArray jsonArr = json.getJSONArray("products");
			JFrame frame = new JFrame("Products");
			String allProducts = "";
			allProducts+="<html>";
			
			// Insert products into string.
			for (int i = 0; i < jsonArr.length(); i++) {
				JSONObject product = jsonArr.getJSONObject(i);
				allProducts+=("--Product ")+(Integer.toString(i+1))+"--<br/>";
				allProducts+=("product id : ")+product.getInt("prodID")+"<br/>";
				allProducts+=("product name : ")+product.getString("prodName")+"<br/>";
				allProducts+=("price : ")+product.getInt("price")+"<br/><br/>";
				}
			allProducts+="</html>";
			
			JLabel label = new JLabel(allProducts);
			label.setFont(new Font("Ariel", Font.PLAIN, 30));
			
			// Show all products in list.
			frame.add(label, BorderLayout.BEFORE_FIRST_LINE);
		    frame.setSize(1000, 500);
		    frame.setVisible(true);
		    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);	    
		}
		catch(Exception err) {
			System.out.println(err);
		}
		//finally:
		//	System.out.println(structureOfJson);
}
}