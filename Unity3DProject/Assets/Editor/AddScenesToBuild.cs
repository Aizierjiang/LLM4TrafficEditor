using UnityEngine;
using UnityEditor;
using System.IO;

public class AddScenesToBuild
{
#if UNITY_EDITOR
    [MenuItem("Tools/Add Build Scenes/All")]
    static void AddAll()
    {
        AddScenes(Application.dataPath);
    }

    [MenuItem("Tools/Add Build Scenes/Only SceneFolders")]
    static void AddOnlyScenesFolders()
    {
        string scenePath = "Scenes"; // Only set the scenes in Scene folder into build
        string path = Path.Combine(Application.dataPath, scenePath);
        AddScenes(path);
    }

    static void AddScenes(string rootPath)
    {
        string path = rootPath;
        string[] files = Directory.GetFiles(path, "*.unity", SearchOption.AllDirectories);
        EditorBuildSettingsScene[] scenes = new EditorBuildSettingsScene[files.Length];
        Debug.Log($"There have been {scenes.Length} scene(s) added in to build settings!");
        //Debug.Log("There have been " + scenes.Length + " scene(s) added in to build settings!");
        for (int i = 0; i < files.Length; ++i)
        {
            int index = files[i].IndexOf("Assets");
            string _path = files[i].Remove(0, index);
            scenes[i] = new EditorBuildSettingsScene(_path, true);
        }
        EditorBuildSettings.scenes = scenes;
    }
#endif
}
