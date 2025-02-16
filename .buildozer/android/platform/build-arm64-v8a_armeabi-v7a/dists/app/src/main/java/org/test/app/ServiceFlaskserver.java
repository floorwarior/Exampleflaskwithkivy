package org.test.app;

import android.content.Intent;
import android.content.Context;
import org.kivy.android.PythonService;


public class ServiceFlaskserver extends PythonService {
    

    @Override
    protected int getServiceId() {
        return 1;
    }
	
    static private void _start(Context ctx, String smallIconName,
                             String contentTitle, String contentText, 
                             String pythonServiceArgument) {
        Intent intent = getDefaultIntent(ctx, smallIconName, contentTitle,
					 contentText, pythonServiceArgument);
        ctx.startService(intent);
    }

    static public void start(Context ctx, String pythonServiceArgument) {
        _start(ctx, "", "TestApp", "Flaskserver", pythonServiceArgument);
    }

    static public void start(Context ctx, String smallIconName,
                             String contentTitle, String contentText, 
                             String pythonServiceArgument) {
	_start(ctx, smallIconName, contentTitle, contentText, pythonServiceArgument);
    }    

    static public Intent getDefaultIntent(Context ctx, String smallIconName,
                                          String contentTitle, String contentText, 
                                          String pythonServiceArgument) {
        Intent intent = new Intent(ctx, ServiceFlaskserver.class);
        String argument = ctx.getFilesDir().getAbsolutePath() + "/app";
        intent.putExtra("androidPrivate", ctx.getFilesDir().getAbsolutePath());
        intent.putExtra("androidArgument", argument);
        intent.putExtra("serviceTitle", "TestApp");
        intent.putExtra("serviceEntrypoint", "background.py");
        intent.putExtra("pythonName", "Flaskserver");
        intent.putExtra("serviceStartAsForeground", "true");
        intent.putExtra("pythonHome", argument);
        intent.putExtra("pythonPath", argument + ":" + argument + "/lib");
        intent.putExtra("pythonServiceArgument", pythonServiceArgument);
        intent.putExtra("smallIconName", smallIconName);
        intent.putExtra("contentTitle", contentTitle);
        intent.putExtra("contentText", contentText);
        return intent;
    }

    @Override
    protected Intent getThisDefaultIntent(Context ctx, String pythonServiceArgument) {
        return ServiceFlaskserver.getDefaultIntent(ctx, "", "", "", 
							     pythonServiceArgument);
    }

    static public void stop(Context ctx) {
        Intent intent = new Intent(ctx, ServiceFlaskserver.class);
        ctx.stopService(intent);
    }
}